from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from .model_fields import LowercaseEmailField


class User(AbstractUser):
    AUTHENTICATED = 'user'
    ADMINISTRATOR = 'admin'
    ROLE_CHOICES = [
        (AUTHENTICATED, 'Аутентифицированный пользователь'),
        (ADMINISTRATOR, 'Администратор'),
    ]
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+\Z',
            ),
        ]
    )
    email = LowercaseEmailField(verbose_name="Email", unique=True)
    first_name = models.CharField(verbose_name="Имя", max_length=150)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150)
    password = models.CharField(verbose_name='Пароль', max_length=150)
    role = models.CharField(verbose_name='Роль', max_length=200,
                            choices=ROLE_CHOICES, default=AUTHENTICATED)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'password']

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = [
            models.UniqueConstraint(
                fields=('username', 'email'), name='unique_username_email'
            )
        ]

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == User.ADMINISTRATOR


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Пользователь - кто подписан',
        verbose_name='subscriber'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='Пользователь - на кого подписан',
        verbose_name='following'
    )

    class Meta:
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_user_author'
            )
        ]
