
from rest_framework import serializers
from .models import Tweet
MAX_LENGTH = 240
class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['user','content', 'pub','hour']

    def validate_content(self, text):
        if len(text)> MAX_LENGTH:
            raise serializers.ValidationError("Too long tweet")
        return text
   