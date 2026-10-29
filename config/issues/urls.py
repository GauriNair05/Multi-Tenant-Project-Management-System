from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrganizationViewSet, OrganizationMembershipViewSet,
    ProjectViewSet, SprintViewSet, TaskViewSet, CommentViewSet,
    DashboardView, ProjectDetailView, create_task
)

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'memberships', OrganizationMembershipViewSet)
router.register(r'projects', ProjectViewSet, basename='project-api')
router.register(r'sprints', SprintViewSet)
router.register(r'tasks', TaskViewSet, basename='task-api')
router.register(r'comments', CommentViewSet)

urlpatterns = [

    path('', DashboardView.as_view(), name='dashboard'),
    path('projects/<uuid:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<uuid:pk>/tasks/create/', create_task, name='create_task'),


    path('api/', include(router.urls)),
]