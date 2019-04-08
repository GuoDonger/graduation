from django.contrib import admin
from user.models import UserProfile, EmailVerify


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', ]


class EmailVerifyAdmin(admin.ModelAdmin):
    list_display = ['email', 'send_type']




admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmailVerify, EmailVerifyAdmin)

