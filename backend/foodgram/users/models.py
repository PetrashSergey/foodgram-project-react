from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import (
    NotDeletedUsernameValidator,
    NotMeUsernameValidator,
    UsernameValidator
)


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        blank=False,
        validators=[
            NotMeUsernameValidator(),
            UsernameValidator(),
            NotDeletedUsernameValidator()
        ]
    )
    email = models.EmailField(verbose_name="Email", unique=True, db_index=True)
    first_name = models.CharField(verbose_name="Имя", max_length=150)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150)
    password = models.CharField(verbose_name='Пароль', max_length=150)

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
        related_name='subscribes',
        verbose_name='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribers',
        verbose_name='Автор',
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'

        constraints = (
            models.CheckConstraint(
                check=~models.Q(user=models.F('author')),
                name='no_self_subscribe'
            ),
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_subscription'
            )
        )

    def __str__(self):
        return f'Подписка {self.user} на {self.author}'
