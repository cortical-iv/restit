#import requests
from django.db import models

#from .utils import search_destiny_player_url, D2_KEY
#from .serializer import SearchPlayerSerializer


class User(models.Model):
    display_name = models.CharField(max_length = 16)
    user_id = models.CharField(max_length = 20)

    def __str__(self):
        return self.display_name

