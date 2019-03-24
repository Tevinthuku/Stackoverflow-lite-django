from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = "You cannot edit or delete this question"

    def has_object_permission(self, request, view, obj):
        print("obj os here")
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
