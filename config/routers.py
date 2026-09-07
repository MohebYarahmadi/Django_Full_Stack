from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.viewsets import UserViewSet
from apps.auth.viewsets.register import RegisterViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')
router.register(r'auth/register', RegisterViewSet, basename='auth-register')

urlpatterns = [
    path('admin/', admin.site.urls),
    # =============================
    path('api/', include(router.urls)),
]
