from django.db import models
from django.utils.text import slugify
from django_prose_editor.fields import ProseEditorField

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Project(models.Model):
    title_en = models.CharField(max_length=200)
    title_uk = models.CharField(max_length=200)
    slug = models.SlugField(max_length=210, unique=True, blank=True)
    excerpt_en = models.TextField()
    excerpt_uk = models.TextField()
    description_en = ProseEditorField()
    description_uk = ProseEditorField()
    tech_stack = models.CharField(max_length=500, help_text="Comma separated technologies")
    repo_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    cover_image = models.ImageField(upload_to='projects/', blank=True, null=True)
    gallery_images = models.JSONField(default=list, blank=True, help_text="List of image URLs for project gallery")
    tags = models.ManyToManyField(Tag, related_name='projects')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title_en = models.CharField(max_length=200)
    title_uk = models.CharField(max_length=200)
    slug = models.SlugField(max_length=210, unique=True, blank=True)
    excerpt_en = models.TextField()
    excerpt_uk = models.TextField()
    content_en = ProseEditorField()
    content_uk = ProseEditorField()
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en

class Note(models.Model):
    title_en = models.CharField(max_length=200, blank=True, null=True)
    title_uk = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=210, unique=True, blank=True)
    content_en = models.TextField()
    content_uk = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.title_en:
            self.slug = slugify(self.title_en)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_en or f"Note {self.id}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
