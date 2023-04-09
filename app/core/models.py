"""
Database Models.
"""

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manager For Users"""
    # **extra_feilds -> we can provide keyword arguments

    def create_user(self, email, password=None,  **extra_feilds):
        """Create, Save & Return new user"""
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_feilds)
        user.set_password(password)
        user.save(using=self._db)  # to support adding mult db

        return user

    # make sure you dont have type inthe name of this fn
    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(self.normalize_email(email), password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # a
    objects = UserManager()  # creates instance of the manger
    USERNAME_FIELD = 'email'

class Recipe(models.Model):

    """
    recipe object.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,

    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    link = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.title
