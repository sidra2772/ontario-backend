from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (
    CreateRoomView,
    ListRoomsView,
    ChatAttachmentView,
    RoomPreviousChatView,
    OnlineStatusUpdateView,
    GroupActivityPreviousChatView,
    RoomView,
    RoomBlockedView,
    ClearRoomChatView,

)
from .views import GroupRoomViewSet, AddAndRemoveGroupMemberAPIView, ReactionViewSet

router = DefaultRouter()

router.register('group-room', GroupRoomViewSet, basename='group-room')
router.register('reaction', ReactionViewSet, basename='reaction')

urlpatterns = [
    path('create-room/', CreateRoomView.as_view(), name='create_room'),
    path('block-room/<int:pk>/', RoomBlockedView.as_view(), name='block_room'),
    path('clear-room-chat/<int:pk>/', ClearRoomChatView.as_view(), name='clear_room_chat'),
    path('get-all-rooms/', ListRoomsView.as_view(), name='list_rooms'),
    path('get-room/<int:pk>/', RoomView.as_view(), name='get_room'),
    path('create-attachment/', ChatAttachmentView.as_view(),
         name='create_attachment'),
    path('update-online-status/', OnlineStatusUpdateView.as_view(),
         name='update_online_status'),
    path('get-room-previous-chat/<int:id>/',
         RoomPreviousChatView.as_view(), name='room_prev_chat'),
    path('get-group-previous-chat/',
         GroupActivityPreviousChatView.as_view(), name='ws_prev_chat'),
    path('add-and-remove-group-member/<int:pk>/',
         AddAndRemoveGroupMemberAPIView.as_view(), name='add_and_remove_group_member'),
    path('', include(router.urls))
]
