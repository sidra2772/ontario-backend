from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = User.objects.get(email=request.data['email'])
        return Response({
            'access': response.data['access'],
            'refresh': response.data['refresh'],
            'user': {
                'id': user.id,
                'email': user.email,
                'is_active': user.is_active,
                'user_type': user.user_type,

            }
        }, status=status.HTTP_200_OK)
