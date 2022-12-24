from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField(
        'image', default='placeholder',
        transformation=[
            {"width": 100, "height": 100, "crop": "fill", "gravity": "face"}
        ]
        )
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username
