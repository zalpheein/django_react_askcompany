from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



















