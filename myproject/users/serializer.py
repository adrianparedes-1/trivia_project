from rest_framework import serializers
from . import models
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Users
        fields = ['user', 'profilePic']