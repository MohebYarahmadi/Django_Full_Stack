from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):
    """
    Custom permission for our users
    Checking that anonymous users can only make the `SAFE_METHODS` requests
    """

    def has_object_permission(self, request, view, obj):
        """On an object level"""
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS

        if view.basename in ['post']:
            return bool(request.user and request.user.is_authenticated)

        return Flase

    def has_permission(self, request, view):
        """On the overall endpoint"""
        if view.basename in ['post']:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS

            return bool(request.user and request.user.is_authenticated)

        return False
