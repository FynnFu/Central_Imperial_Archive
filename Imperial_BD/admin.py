from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name")


admin.site.register(Users, UsersAdmin)