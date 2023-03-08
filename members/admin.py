from django.contrib import admin
from .models import *

# Register your models here.


class SubscribedUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'date_created')


admin.site.register(CustomUser)
admin.site.register(Welcome)
admin.site.register(SubscribedUser, SubscribedUserAdmin)
