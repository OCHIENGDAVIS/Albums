from django.db import models
from accounts.models import UserProfile


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text