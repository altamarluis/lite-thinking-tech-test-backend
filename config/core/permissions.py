from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Allows read-only access to any authenticated user,
    while restricting write operations to admin users only.
    """

    def has_permission(self, request, view) -> bool:
        """
        Checks if the user has permission to perform the request.

        - SAFE_METHODS: Allowed for any authenticated user.
        - Non-safe methods: Allowed only for staff users.

        Args:
            request: Incoming HTTP request.
            view: DRF view handling the request.

        Returns:
            bool: True if access is granted, False otherwise.
        """

        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
