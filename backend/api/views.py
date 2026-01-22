from rest_framework import viewsets, permissions, filters, views
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from content.models import Tag, Project, BlogPost, Note, ContactMessage
from .serializers import (
    TagSerializer, ProjectSerializer, BlogPostSerializer, 
    NoteSerializer, ContactMessageSerializer
)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tags__slug', 'is_featured']
    search_fields = ['title_en', 'title_uk', 'tech_stack']

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.filter(status='published').order_by('-published_at')
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tags__slug']
    search_fields = ['title_en', 'title_uk']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return BlogPost.objects.all().order_by('-created_at')
        return super().get_queryset()

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['tags__slug']
    search_fields = ['title_en', 'title_uk', 'content_en', 'content_uk']

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-created_at')
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'delete', 'update', 'partial_update']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

class UserStatusView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        return Response({
            'is_authenticated': request.user.is_authenticated,
            'is_staff': request.user.is_staff
        })
