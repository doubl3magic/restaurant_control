from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models

from resturant_control.auth_app.managers import ResControlManager
from resturant_control.common.validators import validate_name
from resturant_control.settings import MEDIA_ROOT


class ResControlUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = ResControlManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 20
    FIRST_NAME_MIN_LEN = 3
    LAST_NAME_MAX_LEN = 20
    LAST_NAME_MIN_LEN = 3

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_name,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_name,
        )
    )

    picture = models.ImageField(
        blank=True,
        null=True,
    )

    date_of_birth = models.DateTimeField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        ResControlUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
