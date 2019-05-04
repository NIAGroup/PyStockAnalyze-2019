from django.contrib import admin

# Register your models here.
from .models import UProfile
from .models import UserProfile


class UProfileAdmin(admin.ModelAdmin):
	pass

class UserProfileAdmin(admin.ModelAdmin):
	pass

admin.site.register(UProfile, UProfileAdmin)
admin.site.register(UserProfile, UserProfileAdmin)