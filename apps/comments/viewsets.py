from django.http.response import Http404

from rest_framework.response import Response
from rest_framework import status

from apps.abstracts.viewsets import AbstractViewSet
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer
from apps.auth.permissions import UserPermission


class CommentViewSet(AbstractViewSet):
    http_methods = ('post', 'get', 'put', 'delete')
    permission_classes = (UserPermission,)
    serializer_class = CommentSerializer

    def initial(self, request, *args, **kwargs):
        print("KWARGS:", kwargs)
        print("USER:", request.user, request.user.is_authenticated)
        print("PERMS:", self.get_permissions())
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()

        post_pk = self.kwargs['post_pk']
        if post_pk is None:
            raise Http404
        queryset = Comment.objects.filter(post__public_id=post_pk)

        return queryset

    def get_object(self):
        obj = Comment.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)

        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
