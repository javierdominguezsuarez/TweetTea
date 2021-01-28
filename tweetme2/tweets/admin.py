from django.contrib import admin
from .models import Tweet
# Register your models here.

admin.site.site_header = "Fabio es homo"
#Add table to admin view (modifie-add-delete objects)
admin.site.register(Tweet)