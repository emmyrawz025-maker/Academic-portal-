from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(User)
class SMSUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Role", {"fields": ("role",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Role", {"fields": ("role",)}),)
    list_display = ("username", "first_name", "last_name", "role")

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin): filter_horizontal = ("courses",)
admin.site.register([Department, Student, Course, Semester, Registration, Result])
