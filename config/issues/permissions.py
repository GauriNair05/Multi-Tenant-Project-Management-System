from rest_framework import permissions
from .models import OrganizationMembership

class IsOrganizationMember(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        
        org = None
        if hasattr(obj, 'organization'):
            org = obj.organization
        elif hasattr(obj, 'project'):
            org = obj.project.organization
        elif hasattr(obj, 'task'):
            org = obj.task.project.organization
        elif hasattr(obj, 'task') == False and hasattr(obj, 'body'): # Comment model
            org = obj.task.project.organization

        if not org:
            return False

        
        return OrganizationMembership.objects.filter(
            user=request.user, 
            organization=org
        ).exists()