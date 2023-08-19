from django.contrib import admin
from apps.posts.models import Post, TeamMember, Courses, Benefist


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

@admin.register(Benefist)
class BenefistAdmin(admin.ModelAdmin):
    list_display = ["povtor", "image"]



    







