from django.contrib import admin
from .models import User

'''
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name', 'first_name', 'last_name', 'is_staff', 'is_superuser')
'''

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'username', 'email',  'full_name', 'is_superuser', 'is_staff', 'is_active'
    ]
    fieldsets = (
        (None, {'fields': ('username', 'password', 'full_name', 'first_name', 'last_name', 'email')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permission', {'fields': ('user_permissions',)}),
        ('Status', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    filter_horizontal = ('groups', 'user_permissions')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups__name')

'''class AllowedIPModelAdmin(admin.ModelAdmin):
    list_display = ('address',)
    search_fields = ('address',)

    class Meta:
        model = AllowedIP

admin.site.register(AllowedIP, AllowedIPModelAdmin)'''

# Register your models here.
# admin.site.register(User, CustomUserAdmin)