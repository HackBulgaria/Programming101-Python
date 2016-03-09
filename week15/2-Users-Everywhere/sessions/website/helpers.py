from .models import User


def user_exists(email):
    u = User.objects.filter(email=email)

    return u is not None
