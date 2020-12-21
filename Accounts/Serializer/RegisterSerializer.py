from rest_framework import serializers

from Accounts.Models.UserDetails import user_details


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = user_details.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user