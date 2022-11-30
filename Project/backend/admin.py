from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

# Register your models here.
class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'

class UserAdmin(BaseUserAdmin):
    inlines = (AccountInline,)

admin.site.register(Account)
admin.site.register(Course)
admin.site.register(CourseEnroll)
admin.site.register(Meeting)
admin.site.register(Message)
admin.site.register(ChatRoom)
admin.site.register(Material)
admin.site.register(StudyGroup)
admin.site.register(StudyEnroll)
admin.site.register(Module)
admin.site.register(Friends)
admin.site.register(Invite)
admin.site.register(Announcements)
admin.site.register(FriendRequest)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)