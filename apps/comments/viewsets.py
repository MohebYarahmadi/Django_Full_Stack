from django.http.response import Http404

from rest_framework.response import Response
from rest_framework import status

from apps.abstracts.viewsets import AbstractViewSet
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer
from apps.auth.permissions import UsePermission


class CommentViewSet(AbstractViewSet):
    http_methods = ('post', 'get', 'put', 'delete')
    permission_classes = (UserPermission,)
    serializer_class = CommentSerializer
