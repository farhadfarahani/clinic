from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Doctor, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['doctor', 'author', 'body', 'stars', 'active', ]


@admin.register(Doctor)
class DoctorAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['name', 'active', 'expertise', ]
    inlines = [CommentsInline, ]


@admin.register(Comment)
class CommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['doctor', 'author', 'body', 'stars', 'active', ]
