from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.viewsets import UserViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    # =============================
    path('api/', include(router.urls)),
]
