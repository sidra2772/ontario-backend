from django.db.models import Q
from rest_framework import status
from rest_framework import filters
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
from .utils import search_field_for_partner
from utils.paginations import OurLimitOffsetPagination
from .serializers import ProfileInformationUpdateOnlineStatusSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView
from .models import GroupRoomMessage, Room, RoomMessage, ChatAttachment, OnlineUser
from .serializers import (
    ListRoomSerializer,
    CreateRoomSerializer,
    RoomMessageSerializer,
    ChatAttachmentSerializer,
    GroupRoomMessageSerializer,
    RoomSerializer,

)
from django.db.models import F, Case, When, Value, BooleanField
import logging


class RoomBlockedView(UpdateAPIView):
    """
    This View is used to block a room
    permission_classes:
        IsAuthenticated
    Parameters:
        id: int
    Returns:
        room: object

    """
    permission_classes = [IsAuthenticated]
    queryset = Room.objects.all()

    def get_object(self):
        return Room.objects.get(id=self.kwargs.get('id'))

    def update(self, request, *args, **kwargs):
        room = self.get_object()
        rooms = Room.objects.filter(Q(owner=room.owner, partner=room.partner) |
                                    Q(partner=room.owner, owner=room.partner)
                                    )
        if rooms.exists():
            for room in rooms:
                if not room.is_blocked:
                    room.is_blocked = True
                    room.save()
                    room.blocked_by.add(request.user.profile)
                else:
                    room.is_blocked = False
                    room.save()
                    room.blocked_by.remove(request.user.profile)

        return Response({'detail': 'Room is blocked'}, status=status.HTTP_200_OK)


class ClearRoomChatView(UpdateAPIView):
    """
    This View is used to clear the chat of a room
    permission_classes:
        IsAuthenticated
    Parameters:
        id: int
    Returns:
        room: object

    """
    queryset = Room.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return Room.objects.get(id=self.kwargs.get('id'))

    def update(self, request, *args, **kwargs):
        room = self.get_object()
        room_messages = RoomMessage.objects.filter(room=room).exclude(cleared_by__id=request.user.profile.id)
        if room_messages.exists():
            for room_message in room_messages:
                room_message.cleared_by.add(request.user.profile)
                room_message.is_cleared = True
                room_message.save()
            return Response({'detail': 'Room chat is cleared'}, status=status.HTTP_200_OK)
        return Response({'detail': 'Room chat is already cleared'}, status=status.HTTP_400_BAD_REQUEST)


class RoomView(RetrieveAPIView):
    """
    This View is used to return the room of the request's user.
    permission_classes:
        IsAuthenticated
    Parameters:
        id: int
    Returns:
        room: object

    """
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class ChatAttachmentView(CreateAPIView):
    """
    This View is used to create a chat attachment

    permission_classes:
        IsAuthenticated
    Parameters:
        file: file
    Returns:
        attachment: object


    """

    def get_serializer_context(self):
        context = {"request": self.request}
        return context

    serializer_class = ChatAttachmentSerializer
    queryset = ChatAttachment.objects.all()


class GroupActivityPreviousChatView(ListAPIView):
    """
    This View is used to give the previous messages of group
    activity. If the workspace_is in query params is given then
    it will return the messages of that group room else it will
    return all the messages of all group rooms.
    permission_classes:
        IsAuthenticated
    Parameters:
        group_id: int
    Returns:
        messages: list

    """
    serializer_class = GroupRoomMessageSerializer
    pagination_class = OurLimitOffsetPagination

    def get_queryset(self):
        group_id = self.request.GET.get('group_id')
        queryset = GroupRoomMessage.objects.all().order_by('-created_at')

        if group_id:
            queryset = queryset.filter(room__id=group_id)
            # Use conditional expression to update is_read field based on the filter condition
            queryset.update(
                is_read=Case(
                    When(room__id=group_id, then=True),
                    default=F('is_read'),
                    output_field=bool,
                )
            )
        else:
            # Update all messages where is_read=False
            queryset.update(is_read=Case(default=True, output_field=bool))
        return queryset


class CreateRoomView(CreateAPIView):
    """
    This View is used to create a room for personal chat between
    buyer and seller.
    permission_classes:
        IsAuthenticated
    Parameters:
        partner: int
        owner: int

    Returns:
        room: object

    """
    serializer_class = CreateRoomSerializer
    queryset = Room.objects.all()

    def get_serializer_context(self):
        context = {"request": self.request}
        return context


class ListRoomsView(ListAPIView):
    """
    This View is used return all rooms of the request's user.
        - If request's user is buyer, it will return all those rooms
          in which he is added as owner
        - If request's user is seller, it will return all those rooms
          in which he is added as partner
    permission_classes: 
        IsAuthenticated
    Parameters: 
        None
    search_fields:
        partner__user__first_name
        partner__user__last_name
        partner__user__username
    Returns:
        rooms: list

    """

    serializer_class = ListRoomSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = search_field_for_partner

    def get_queryset(self):
        rooms = Room.objects.filter(
            Q(partner=self.request.user.profile) | Q(
                owner=self.request.user.profile)
        ).order_by('-updated_at')
        return rooms

    def get_serializer_context(self):
        context = {
            "request": self.request,
            "user": self.request.user
        }
        return context


class OnlineStatusUpdateView(UpdateAPIView):
    """
    This View is used to update the online status of the user
    permission_classes:
        IsAuthenticated
    Parameters:
        is_online: bool
    Returns:
        profile: object

    """
    serializer_class = ProfileInformationUpdateOnlineStatusSerializer

    def get_object(self):
        return self.request.user.profile

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.get_object(), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            try:
                online_user = OnlineUser.objects.filter(
                    profile=request.user.profile).exists()
                if online_user:
                    OnlineUser.objects.filter(
                        profile=request.user.profile).delete()

            except OnlineUser.DoesNotExist:
                return Response({'detail': 'User is not online'}, status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoomPreviousChatView(ListAPIView):
    """
    This View is used to give the previous messages of room
    permission_classes:
        IsAuthenticated
    Parameters:
        id: int
    Returns:
        messages: list

    """

    serializer_class = RoomMessageSerializer
    pagination_class = OurLimitOffsetPagination

    def list(self, request, *args, **kwargs):
        room_id = self.kwargs.get('id')
        try:
            messages = RoomMessage.objects.filter(room_id=room_id).annotate(
                _is_read=Case(
                    When(is_read=False, then=Value(True)),
                    default=Value(False),
                    output_field=BooleanField(),
                )
            ).order_by('-created_at')

            # Update is_read field for unread messages in the room
            messages.update(is_read=True)

            # Prefetch related data
            messages = messages.prefetch_related('attachment', 'reactions').select_related('order')

            # Serialize messages
            chat_list_serializer = self.serializer_class(messages, many=True)
            return Response(chat_list_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(e)
            return Response({'message': "something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
