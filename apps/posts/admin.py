from django.contrib import admin
from apps.posts.models import Post, TeamMember, Courses, Front, Back, Ux_ui, Android


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "status"]
    list_filter = ["title", "status"]
    list_editable = ["status"]

@admin.register(TeamMember)
class TeamemberAdmin(admin.ModelAdmin):
    list_display = ["name", "role", "image"]

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ["front_end", "back_end", "ux_ui", "android"]

@admin.register(Front)
class FrontAdmin(admin.ModelAdmin):
    list_display = ["front"]

@admin.register(Back)
class BackAdmin(admin.ModelAdmin):
    list_display = ["back"]


@admin.register(Ux_ui)
class Ux_uiAdmin(admin.ModelAdmin):
    list_display = ["ux_ui"]


@admin.register(Android)
class AndroidAdmin(admin.ModelAdmin):
    list_display = ["android"]





