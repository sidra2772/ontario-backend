from django.template.defaultfilters import slugify

from channels.generic.websocket import (
    AsyncJsonWebsocketConsumer
)
from notification.utils import send_notification, create_notification_object

from asgiref.sync import async_to_sync, sync_to_async

from .utils import (
    is_room_member,
    is_user_online,
    set_user_online,
    all_online_users,
    is_user_online_check,
    get_chat_rooms_updated,
    is_group_room_member,
    create_ws_room_msg_object,
    create_room_message_object,
    create_online_user_instance,
    delete_online_user_instance,
    delete_online_user_instance_check,
)


class GroupActivityAsyncConsumer(AsyncJsonWebsocketConsumer):
    """ 
    This consumer is used to handle the messages sent to the Group activity chat.
    It is a async consumer. If the request's user does not belongs to the group room
    then he is not allowed to connect and send the messages.
    """

    async def connect(self):

        await self.accept()
        # kwargs = self.scope["url_route"]["kwargs"]
        query_params = dict(
            (x.split('=') for x in self.scope['query_string'].decode().split("&")))
        group = query_params.get('group')
        user = self.scope['user']

        if user.is_authenticated and group:
            try:
                is_member, group_room = await is_group_room_member(user, group)
                if is_member:

                    self.group_name = slugify(
                        f'{group_room.name}-{group_room.id}')
                    await self.channel_layer.group_add(self.group_name, self.channel_name)
                else:
                    await self.send_json("You are not member of this group room")
                    await self.close(code=4000)
            except:
                await self.send_json("Invalid group id")
                await self.close(code=4000)
        else:
            await self.send_json("valid token and group is required in params to establish the connection!")
            await self.close(code=4000)

    async def receive_json(self, content, **kwargs):
        group = content.get('group')
        message = content.get('message')
        is_file = content.get('is_file', False)
        attachment_file = content.get('file', None)
        is_report = content.get('is_custom_order', False)
        report = content.get('order', None)

        user = self.scope['user']
        if user.is_authenticated:
            message_obj = await create_ws_room_msg_object(group, is_report, report, user, message, is_file,
                                                          attachment_file)

            message = message_obj

            await self.channel_layer.group_send(
                self.group_name, {
                    'type': 'chat.message',
                    'message': message
                }
            )
            print(message['id'])
            if not is_report:
                send_notification_data = await create_notification_object(

                    sender=user,
                    message=message['id'],
                    heading='sent a message',
                    plain_text='sent a',
                    notification_type='sent_message',
                    description=message['message'])
                await sync_to_async(send_notification)(send_notification_data)


        else:
            await self.send_json("login required")

    async def chat_message(self, event):
        await self.send_json(event['message'])

    async def disconnect(self, code):
        # When disconnected remove the user from group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name,
        )


class DashboardChatConsumer(AsyncJsonWebsocketConsumer):
    """
        This consumer is being used for personal chat. It is  async consumer.
        There are only two users in the room of this consumer between which personal
        chat will be executed. If the request's user do not belong to the
        group room then he is not allowed to connect and s
    end the messages.
    """

    async def connect(self):
        await self.accept()
        query_params = dict(
            (x.split('=') for x in self.scope['query_string'].decode().split("&")))
        room_id = query_params.get('room_id')
        user = self.scope['user']

        if user.is_authenticated and room_id:
            try:
                is_member, group_name = await is_room_member(user, room_id)
                if is_member:
                    self.group_name = group_name
                    await self.channel_layer.group_add(self.group_name, self.channel_name)
                else:
                    await self.send_json("You are not member of this room")
                    await self.close(code=4000)
            except Exception as e:
                await self.send_json({"message": str(e)})
                await self.close(code=4000)
        else:
            await self.send_json("valid token and room_id is required in params to establish the connection!")
            await self.close(code=4000)

    async def receive_json(self, content, **kwargs):
        room = content.get('room', )
        message = content.get('message')
        is_file = content.get('is_file', False)
        attachment_file = content.get('file', None)
        order = content.get('order', None)
        is_order = content.get('is_custom_order', False)

        user = self.scope['user']

        if user.is_authenticated:
            is_member, group_name = await is_room_member(user, room)

            if is_member:

                message_obj = await create_room_message_object(
                    room=room,
                    user=user,
                    message=message,
                    is_file=is_file,
                    file_attachment=attachment_file,
                    order=order,
                    is_custom_order=is_order,
                )

                message = message_obj

                await self.channel_layer.group_send(
                    group_name, {
                        'type': 'chat.message',
                        'message': message
                    }
                )

                if not is_order:
                    send_notification_data = await create_notification_object(

                        sender=user,
                        message=message_obj['id'],

                        heading='sent a message',
                        plain_text='sent a',
                        notification_type='sent_message',
                        description=message['message'])
                    await sync_to_async(send_notification)(send_notification_data)


            else:
                await self.send_json("Invalid room id, i.e you are not the member of the given room")
                await self.close(code=4000)
        else:
            await self.send_json("login required")

    async def chat_message(self, event):

        await self.send_json(event['message'])

    async def disconnect(self, code):
        # When disconnected remove the user from group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name,
        )


class OnlineStatusConsumer(AsyncJsonWebsocketConsumer):
    """
        This consumer is used to set the online and offline status of a user.
        It is  async consumer.
    """

    async def connect(self):

        user = self.scope['user']

        if user.is_authenticated:

            await self.accept()
            self.group_name = "online_users"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await create_online_user_instance(self.channel_name, user)
            user_online_flag = await is_user_online(user)
            if user_online_flag:
                await set_user_online(user)
                all_online_user = await all_online_users(self.channel_name)
                await self.channel_layer.group_send(
                    self.group_name, {
                        'type': 'user.is_offline',
                        'message': all_online_user
                    }

                )
        else:
            await self.send_json("login required")
            await self.close(code=4000)

    async def receive_json(self, content, **kwargs):
        user = self.scope['user']

        if user.is_authenticated:
            self.group_name = "online_users"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            user_online_flag = await is_user_online(user)
            if user_online_flag:
                all_online_user = await all_online_users(self.channel_name)
                await self.channel_layer.group_send(
                    self.group_name, {
                        'type': 'user.is_offline',
                        'message': all_online_user
                    }

                )
        else:
            await self.send_json("login required")
            await self.close(code=4000)

    async def disconnect(self, code):
        # When disconnected remove the user from group
        user = self.scope['user']

        if user.is_authenticated:
            profile_id = await delete_online_user_instance(user)

            self.is_online_status = await delete_online_user_instance_check(user)

            await self.channel_layer.group_send(
                self.group_name, {
                    'type': 'user.is_offline',
                    'message': [{
                        "profile_id": profile_id,
                        "is_online": self.is_online_status,
                    }]
                }
            )
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name,
            )

    async def user_is_offline(self, event):
        await self.send_json(event['message'])


class ChatUpdateConsumers(AsyncJsonWebsocketConsumer):
    async def connect(self):

        await self.accept()
        user = self.scope['user']
        if user.is_authenticated:
            self.group_name = "chat_updates"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
        else:
            await self.send_json("login required")
            await self.close(code=4000)

    async def disconnect(self, code):
        # When disconnected remove the user from group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name,
        )

    async def chat_update(self, event):
        await self.send_json(event['message'])

    async def receive_json(self, content, **kwargs):
        user = self.scope['user']
        if user.is_authenticated:

            get_rooms_chat_update_object = await get_chat_rooms_updated(user, self.scope)
            message = get_rooms_chat_update_object

            await self.channel_layer.group_send(
                'chat_updates', {
                    'type': 'chat.update',
                    'message': message
                }
            )

        else:
            await self.send_json("login required")

    async def chat_message(self, event):
        await self.send_json(event['message'])

    async def disconnect(self, code):
        # When disconnected remove the user from group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name,
        )


class UserOnlineStatusConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        user = self.scope['user']

        if user.is_authenticated:
            self.group_name = "online_users_status"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
        else:
            await self.send_json("login required")
            await self.close(code=4000)

    async def receive_json(self, content, **kwargs):
        user = self.scope['user']
        user_profile_id = content['profile_id']
        if user.is_authenticated:
            online_status = await is_user_online_check(user_profile_id)

            if online_status:
                await self.channel_layer.group_send(
                    'online_users_status', {
                        'type': 'user.online.status',
                        'message': [{
                            "profile_id": user_profile_id,
                            "is_online": True
                        }]
                    })
            else:
                await self.channel_layer.group_send(
                    'online_users_status', {
                        'type': 'user.online_status',
                        'message': [{
                            "profile_id": user_profile_id,
                            "is_online": online_status
                        }]
                    }
                )

        else:
            await self.send_json("login required")

    async def disconnect(self, code):
        # When disconnected remove the user from group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name,
        )

    async def user_online_status(self, event):
        await self.send_json(event['message'])
