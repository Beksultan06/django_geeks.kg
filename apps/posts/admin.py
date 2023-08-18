from django.contrib import admin
from apps.posts.models import Post, Courses, Front, Back, Ux_ui, Android


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "status"]
    list_filter = ["title", "status"]
    list_editable = ["status"]


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ["front_end", "back_end", "ux_ui", "android"]

@admin.register(Front)
class FrontAdmin(admin.ModelAdmin):
    list_display = ["front"]



