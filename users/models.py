from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    #if we delete the profile it still keep the user but when delete the user we delete the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'

