from django.core.exceptions import ValidationError


def validate_name(name):
    for s in name:
        if not s.isalpha():
            raise ValidationError("A name can not contain numbers or symbols!")
    return True
