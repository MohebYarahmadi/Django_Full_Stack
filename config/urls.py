from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers

from apps.users.viewsets import UserViewSet
from apps.auth.viewsets import (
    RegisterViewSet,
    LoginViewSet,
    RefreshViewSet,
)
from apps.posts.viewsets import PostViewSet
from apps.comments.viewsets import CommentViewSet


router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

router.register(r'posts', PostViewSet, basename='post')

# Nested Routers
posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comment')


urlpatterns = [
    path('admin/', admin.site.urls),
    # =============================
    path('api/', include(router.urls)),
    path('api/', include(posts_router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
