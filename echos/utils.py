from django.http import HttpResponseForbidden
from .models import Echo


def check_owner(func):
    def wrapper(*args, **kwargs):
        echo = Echo.objects.get(pk=kwargs['echo_pk'])
        if echo.user != args[0].user:
            return HttpResponseForbidden('Error 403 - Forbidden')
        return func(*args, **kwargs)
    return wrapper
