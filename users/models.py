from abc import ABC

from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, user_type, password):
        if not email:
            raise ValueError('Users must have a valid email address')
        user = self.model(
            email=self.normalize_email(email)
        )
        user.user_type = user_type
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
            user_type='admin'
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    user_type = models.CharField(max_length=30,
                                 choices=(('customer', 'customer'),
                                          ('employee', 'employee'),
                                          ('admin', 'admin')))
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    @staticmethod
    def has_perm(self):
        return True

    @staticmethod
    def has_module_perms(self):
        return True

    @property
    def is_staff(self):
        return self.is_admin
