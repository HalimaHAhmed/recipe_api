"""
views for the recipe apis
"""


from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated


from core.models import Recipe

from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
    """
    view for manage recipe api's
    """


    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        retrive recipes for authenticated user
        """
        return self.queryset.filter(user=self.request.user).order_by('-id')
    def get_serializer_class(self):
        """
        return the serializer class or request
        """

        if self.action == 'list':
            return serializers.RecipeSerializer
        return self.serializer_class