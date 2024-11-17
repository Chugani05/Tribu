from django.http import HttpResponseForbidden
from .models import Wave


def check_owner(func):
    def wrapper(*args, **kwargs):
        wave = Wave.objects.get(pk=kwargs['wave_pk'])
        if wave.user != args[0].user:
            return HttpResponseForbidden('Error 403 - Forbidden')
        return func(*args, **kwargs)
    return wrapper