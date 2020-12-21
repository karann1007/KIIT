from Accounts.Models.UserDetails import user_details
from rest_framework import serializers

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields = ('username', 'email', 'password')