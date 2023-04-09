from django.shortcuts import render

"""
views for the user api
"""

# view part
from rest_framework import generics, authentication,permissions

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """
    create a new user in the system
    """

    serializer_class = UserSerializer



class CreateTokenView(obtain_auth_token):
    """
    create a new auth token for a user
    """

    serializer_class =AuthTokenSerializer
    renderer_classes =api_settings.DEFAULT_RENDERER_CLASSES

    def ManageUserView(generics,RetrieveUpdateApiView):
        """
        manage the authenticated user
        """

        serializer_class = UserSerializer
        authentication_classes = [authentication.TokenAuthentication]

        permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        retrieve and return the authenticated user
        """

        return self.request.user
