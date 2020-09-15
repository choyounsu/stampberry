from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Org_User
# Register your models here.


admin.site.register(Org_User, UserAdmin)