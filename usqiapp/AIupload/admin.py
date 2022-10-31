from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea











class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'first_name', 'phone', 'promo')
    list_filter = ('email', 'phone', 'first_name', 'is_active', 'is_staff', 'promo')
    ordering = ('-start_date',)
    list_display = ('email', 'phone', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'phone', 'first_name', 'help_phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'promo')}),
        ('Personal', {'fields': ('about','goal')})
    )
    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'phone', 'help_phone' 'password1', 'password2', 'is_active', 'is_staff', 'promo', 'goal')}
         ),
    )


admin.site.register(NewUser, UserAdminConfig)