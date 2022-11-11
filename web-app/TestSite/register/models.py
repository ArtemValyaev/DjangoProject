from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='profile_user')
    profile_img = models.ImageField(upload_to='images/profile_img', default='static/main/images/profile-photo.png')
    bio = models.TextField('О себе', max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.profile}'