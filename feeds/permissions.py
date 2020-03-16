from rest_framework import permissions


class PostOwnStatus(permissions.BasePermission):
    """Allow the user to post their own status"""

    def has_object_permission(self, request, view, obj):
        '''Checks the user is trying to update their status'''

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id