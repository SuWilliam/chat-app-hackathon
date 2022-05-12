from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default=None)

    def __str__(self):
        return self.text