#import requests
from django.db import models


class User(models.Model):
    """Model for the user object: display_name and user_id are unique together."""
    display_name = models.CharField(max_length = 16, blank = False)
    user_id = models.CharField(max_length = 20, blank = False)
    class Meta:
        unique_together = ('display_name', 'user_id')  #these two are unique

    def __str__(self):
        return self.display_name

