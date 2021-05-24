
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.core import serializers
from knox.models import AuthToken
from rest_framework import status
from rest_framework.response import Response

from Accounts.Models.UserDetails import user_details
from util.Validator import Validator


class UserDetailService:

    def create_user(self, data):
        new_user = user_details()
        self.__validate_input(new_user, data)
        new_user = user_details()
        # new_user.first_name = data['first_name']
        # new_user.last_name = data['last_name']
        new_user.email = data['email']
        new_user.username = data['username']
        new_user.usertype = data['usertype']
        new_user.name = data['name']
        new_user.address = data['address']
        new_user.mobile = data['mobile']
        new_user.password = make_password(data['password'])
        zone_text = ""
        for x in data['zone']:
            zone_text += x + " , "
        zone_text = zone_text[:-3]
        new_user.zone = zone_text
        with transaction.atomic():
            new_user.save()
            return Response({
                "user": serializers.serialize('json', [new_user, ]),
                "token": AuthToken.objects.create(new_user)[1]
            }, status=status.HTTP_201_CREATED)

    def update_user(self, data, new_user):
        self.__validate_input(new_user,data)
        # new_user.first_name = data['first_name']
        # new_user.last_name = data['last_name']
        new_user.email = data['email']
        new_user.username = data['username']
        new_user.usertype = data['usertype']
        new_user.name = data['name']
        new_user.address = data['address']
        new_user.mobile = data['mobile']
        new_user.password = make_password(data['password'])
        zone_text = ""
        for x in data['zone']:
            zone_text += x + " , "
        zone_text = zone_text[:-3]
        new_user.zone = zone_text
        with transaction.atomic():
            new_user.save()
            return Response({ "name" : new_user.name ,
                      "user_id" :new_user.id,
                      "email": new_user.email,
                      "mobile": new_user.mobile ,
                      "address": new_user.address ,
                      "zone" : new_user.zone.split(',') if new_user.zone is not None else new_user.zone ,
                      "usertype" : new_user.usertype ,
                       "username" : new_user.username,
                      "is_active" : new_user.is_active
    }, status=status.HTTP_200_OK)

    def __validate_input(self, new_user, data):
        Validator.validate_string(data.get('password'), "Password cannot be empty!")
        Validator.validate_string(data.get('username'), "Username cannot be empty!")
        Validator.validate_string(data.get('usertype'), "Usertype cannot be empty!")
        Validator.validate_zone(data.get('zone'), "Zone cannot be empty!")
        Validator.validate_string(data.get('name'), "name cannot be empty!")
        Validator.validate_string(data.get('email'), "Email cannot be empty!")
        Validator.validate_username(new_user, data.get('username'), "Duplicate Username!")
        Validator.validate_email(new_user, data.get('email'), "Duplicate Email!")
