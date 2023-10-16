from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *


class UniversesAdmin(admin.ModelAdmin):
    list_display = ("name", )


class UsersAdmin(admin.ModelAdmin):
    list_display = ("first_name", "id")


class NamesAdmin(admin.ModelAdmin):
    list_display = ("name", "user")
    list_filter = ("user", )


admin.site.register(Universes, UniversesAdmin)
admin.site.register(Person)
admin.site.register(Levels)
admin.site.register(Directive)
admin.site.register(Users, UsersAdmin)
admin.site.register(Levels_pyramid)
admin.site.register(Names, NamesAdmin)
