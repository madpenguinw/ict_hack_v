from django.core.exceptions import ValidationError

NOT_CORRECT_NAME = [
    'me',
    'login',
    'username',
]


def validate_username(value):
    if value in NOT_CORRECT_NAME:
        raise ValidationError(
            ('Имя пользователя "%(value)s" не доступно.', {'value': value})
        )
