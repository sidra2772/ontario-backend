from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from core.serializers import UserDetailSerializer

User = get_user_model()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """User detail api instant """
    queryset = User.objects.all().select_related('profile')
    serializer_class = UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
