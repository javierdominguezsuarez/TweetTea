from django.db import models
from django.db.models.fields import TextField
from utils.models import AppBaseModel
# Create your models here

# tweet composed by content , image, date and hour 
class Tweet (AppBaseModel):
    content = models.TextField(blank = False, null =False)
    image = models.FileField(upload_to='images/',blank= True , null = True)
