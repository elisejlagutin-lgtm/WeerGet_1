from django.contrib import admin

from .models import Message, GroupsUser

admin.site.register(Message)
admin.site.register(GroupsUser)
