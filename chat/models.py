from django.db import models
from coresite.mixin import AbstractTimeStampModel

GROUP_TYPE_CHOICES = (
    ('group', 'Group'),
    ('report', 'Report'),

)


class GroupRoom(AbstractTimeStampModel):
    profile = models.ManyToManyField(
        "userprofile.UserProfile", related_name='profile_rooms')
    group_creator = models.ForeignKey(
        "userprofile.UserProfile", on_delete=models.CASCADE, related_name='creator_rooms')
    group_admin = models.ManyToManyField(
        'userprofile.UserProfile', related_name='group_admin_rooms')
    group_moderator = models.ManyToManyField(
        'userprofile.UserProfile', related_name='group_moderator_rooms')
    name = models.CharField(max_length=255)
    group_type = models.CharField(max_length=255, default='group', choices=GROUP_TYPE_CHOICES)

    def __str__(self):
        return self.name


class ChatAttachment(AbstractTimeStampModel):
    file = models.FileField(upload_to="chat-attachments")
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.CharField(max_length=255, blank=True, null=True)


REACTION_CHOICES = (
    ('like', 'like'),
    ('love', 'love'),
    ('haha', 'haha'),
    ('wow', 'wow'),
    ('sad', 'sad'),
    ('angry', 'angry'),
)


class Reaction(AbstractTimeStampModel):
    profile = models.ForeignKey(
        "userprofile.UserProfile", on_delete=models.CASCADE, related_name='profile_reactions')
    room_message = models.ForeignKey(
        "chat.GroupRoomMessage", on_delete=models.CASCADE, related_name='room_message_reactions', null=True,
        blank=True)
    message = models.ForeignKey(
        "chat.RoomMessage", on_delete=models.CASCADE, related_name='message_reactions', null=True, blank=True)
    reaction = models.CharField(
        max_length=255, choices=REACTION_CHOICES, default='like')


class GroupRoomMessage(AbstractTimeStampModel):
    room = models.ForeignKey(
        GroupRoom, on_delete=models.CASCADE, related_name='ws_room_messages')
    profile = models.ForeignKey(
        "userprofile.UserProfile", on_delete=models.CASCADE, related_name='profile_ws_room_messages')
    message = models.TextField(max_length=1000, null=True, blank=True)
    reactions = models.ManyToManyField(
        Reaction, related_name='reaction_ws_room_messages', blank=True)

    attachment = models.ForeignKey(ChatAttachment, on_delete=models.CASCADE,
                                   related_name='attachment_ws_room_messages', null=True, blank=True)
    report = models.ForeignKey(
        "helpandsupport.Report", on_delete=models.CASCADE, related_name='report_ws_room_messages', null=True,
        blank=True)
    is_report = models.BooleanField(default=False)
    is_file = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    is_offer_attached = models.BooleanField(default=False)


class Room(AbstractTimeStampModel):
    owner = models.ForeignKey(
        "userprofile.UserProfile", on_delete=models.CASCADE, related_name='owner_rooms')
    partner = models.ForeignKey(
        "userprofile.UserProfile", on_delete=models.CASCADE, related_name='partner_rooms')
    is_blocked = models.BooleanField(default=False)
    dispute = models.ForeignKey(
        "helpandsupport.Report", on_delete=models.CASCADE, related_name='dispute_rooms', null=True, blank=True)
    blocked_by = models.ManyToManyField(
        "userprofile.UserProfile", related_name='blocked_rooms', blank=True)


class RoomMessage(AbstractTimeStampModel):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='room_messages', null=True, blank=True)
    owner = models.ForeignKey(
        "userprofile.UserProfile", on_delete=models.CASCADE, related_name='owner_room_messages', null=True, blank=True)
    message = models.TextField(max_length=90000, null=True, blank=True)
    attachment = models.ForeignKey(ChatAttachment, on_delete=models.CASCADE,
                                   related_name='attachment_room_messages', null=True, blank=True)
    reactions = models.ManyToManyField(
        Reaction, related_name='reaction_room_messages', blank=True)
    order = models.ForeignKey(
        "dashboard.Orders", on_delete=models.CASCADE, related_name='order_room_messages', null=True, blank=True)
    cleared_by = models.ManyToManyField(
        "userprofile.UserProfile", related_name='cleared_room_messages', blank=True)
    is_cleared = models.BooleanField(default=False)
    is_custom_order = models.BooleanField(default=False)
    is_file = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)


class OnlineUser(AbstractTimeStampModel):
    profile = models.ForeignKey(
        "userprofile.UserProfile",
        on_delete=models.CASCADE,
        related_name='online_profile',
        blank=True,
        null=True)
    channel_id = models.CharField(max_length=500)
