from django.conf import settings
from django.db import models
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(
        blank=True, null=True, upload_to='avatars', default='avatars/noavatar.png'
    )
    bio = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('users:user-detail', kwargs=dict(username=self.user.username))

    