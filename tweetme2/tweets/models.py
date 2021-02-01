from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from rest_framework.serializers import ModelSerializer
from utils.models import AppBaseModel
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here
User = get_user_model()
# tweet composed by content , image, date and hour 
class TweetManager(models.Manager):
    def tweet_count(self):
        print("hellow word")
class Tweet (AppBaseModel):
    objects = TweetManager()
    user = models.ForeignKey(User,on_delete=models.CASCADE )
    content = models.TextField(blank = False, null =False)
    image = models.FileField(upload_to='images/',blank= True , null = True)
    #likes = models.ManyToManyField(User, related_name='tweet_user')
    