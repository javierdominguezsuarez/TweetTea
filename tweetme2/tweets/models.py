from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from utils.models import AppBaseModel
from django.conf import settings
# Create your models here
User = settings.AUTH_USER_MODEL
# tweet composed by content , image, date and hour 
class Tweet (AppBaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE )
    content = models.TextField(blank = False, null =False)
    image = models.FileField(upload_to='images/',blank= True , null = True)
    #likes = models.ManyToManyField(User, related_name='tweet_user')
    