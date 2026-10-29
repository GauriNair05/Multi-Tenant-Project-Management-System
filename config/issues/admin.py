from django.contrib import admin
from .models import Organization, OrganizationMembership, Project, Sprint, Task, Comment

admin.site.register(Organization)
admin.site.register(OrganizationMembership)
admin.site.register(Project)
admin.site.register(Sprint)
admin.site.register(Task)
admin.site.register(Comment)