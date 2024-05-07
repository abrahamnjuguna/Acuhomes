from django.contrib import admin
from .models import *




class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 5


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'location', 'completion_date', 'client', 'status')
    search_fields = ['title', 'location', 'client', 'status']
    inlines = [ProjectImageInline]


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', )
    search_fields = ('first_name',)