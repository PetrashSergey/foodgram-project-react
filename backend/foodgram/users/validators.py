from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class UsernameValidator(validators.RegexValidator):
    regex = r"^[a-z0-9@+-]+$"
    message = (
        "Вы ввели невалидный username!\n"
        "Username может состоять из символов латинского "
        "алфавита [a-z], цифр [0-9] и спецсимволов: [ @ + - ]"
    )
    flags = 0


@deconstructible
class NotMeUsernameValidator(validators.RegexValidator):
    regex = r"^(?!Me$|me$|ME$|mE$).*$"
    message = ("Userneme не может быть - Me")
    flags = 0


@deconstructible
class NotDeletedUsernameValidator(validators.RegexValidator):
    regex = r"^(?!(?i:deleted)).*$"
    message = ("Userneme не может быть - Deleted")
    flags = 0
