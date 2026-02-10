"""
URL configuration for vikhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

def api_root(request):
    """API Root - показує доступні endpoints"""
    return JsonResponse({
        'message': 'Welcome to ViktorHub API',
        'version': '1.0',
        'endpoints': {
            'projects': '/api/projects/',
            'blog_posts': '/api/posts/',
            'notes': '/api/notes/',
            'tags': '/api/tags/',
            'contact': '/api/contact/',
            'admin': '/admin/',
            'api_docs': '/api/',
        },
        'authentication': {
            'token': '/api/token/',
            'refresh': '/api/token/refresh/',
        },
        'frontend': 'http://localhost:3000'
    })

def custom_logout(request):
    """Custom logout що редиректить на фронтенд"""
    from django.contrib.auth import logout
    logout(request)
    return redirect('http://localhost:3000')

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('accounts/logout/', custom_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

