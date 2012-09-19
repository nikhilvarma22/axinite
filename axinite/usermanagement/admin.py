from django.contrib import admin
from axinite.usermanagement.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name")
admin.site.register(UserProfile,UserProfileAdmin)