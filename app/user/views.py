"""Views from the user api"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)
class CreateUserView(generics.CreateAPIView):
    """a new sys"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """new auth toke"""
    serializer_class = AuthTokenSerializer
    render_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage"""
    serializer_class = UserSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """get"""
        return self.request.user

