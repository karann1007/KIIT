from django.contrib import admin

# Register your models here.
from Accounts.Models.UserDetails import user_details

admin.site.register(user_details)