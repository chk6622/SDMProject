# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from UserManagement.models import CustomUserCreationForm, CustomUserChangeForm
from UserManagement.models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('project','nationality','hobby','slack_account')}),
    )

#     list_display = ['email', 'username',]
    
admin.site.register(CustomUser, CustomUserAdmin)
