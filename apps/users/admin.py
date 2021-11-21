from django.contrib import admin

from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model=User
    ordering=('date_joined',)
    list_display=('email','first_name','last_name')
    fieldsets = (
        (None, {'fields': ('email', 'first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name' , 'last_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(User,UserAdminConfig)