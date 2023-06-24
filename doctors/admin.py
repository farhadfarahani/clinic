from django.contrib import admin

from .models import Doctor, Comment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'expertise', ]


@admin.register(Comment)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'author', 'body', 'stars', 'active', ]
