from django.contrib import admin
from .models import Tag, Project, BlogPost, Note, ContactMessage

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'tags')
    search_fields = ('title_en', 'title_uk', 'tech_stack')
    prepopulated_fields = {'slug': ('title_en',)}
    filter_horizontal = ('tags',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'status', 'published_at')
    list_filter = ('status', 'tags')
    search_fields = ('title_en', 'title_uk')
    prepopulated_fields = {'slug': ('title_en',)}
    filter_horizontal = ('tags',)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'created_at')
    search_fields = ('title_en', 'title_uk', 'content_en', 'content_uk')
    filter_horizontal = ('tags',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
