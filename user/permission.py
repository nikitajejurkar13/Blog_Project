from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message= "only owner can access this resource"
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role== 'owner'
    
    
class IsEmployee(BasePermission):
    message= "only employee can access this resource"
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role== 'employee'
        