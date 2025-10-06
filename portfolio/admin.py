from django.contrib import admin
from .models import Project, Profile, Skill, Experience


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "location")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level")
    list_filter = ("level",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "start_date", "end_date")
    list_filter = ("company",)
