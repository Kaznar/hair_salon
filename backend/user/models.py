from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password, is_staff=False, is_active=False, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_active=is_active, is_staff=is_staff, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        return self.create_user(email, password, is_active=True, is_staff=True, is_superuser=True, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        ordering = ('id', 'email',)

    def __str__(self):
        return self.email



