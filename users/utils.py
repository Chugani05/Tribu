from django.http import HttpResponseForbidden
from django.contrib.auth.models import User


def check_owner(func):
    def wrapper(*args, **kwargs):
        user = User.objects.get(username=args[1])
        if user != args[0].user:
            return HttpResponseForbidden('Error 403 - Forbidden')
        return func(*args, **kwargs)
    return wrapper
