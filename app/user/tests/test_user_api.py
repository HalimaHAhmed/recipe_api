"""
tests for the user api

"""

from django.test import testcases

from django.contrib.auth import get_user_model

from django.urls import reverse

from rest_framework.test import APIClient

from rest_framework import status

CREATE_USER_URL = reverse('user:create')


    # def create_user(**params):
    #     """"""