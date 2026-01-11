from django.contrib import admin
from .models import Project, Skill, Hero, About

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')  # removed 'created_at'
    search_fields = ('title',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')  # removed 'icon_class'
    list_filter = ('level',)
    search_fields = ('name',)

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('heading',)
