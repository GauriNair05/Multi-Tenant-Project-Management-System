from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, DetailView
from rest_framework import viewsets
from .models import Organization, OrganizationMembership, Project, Sprint, Task, Comment
from .serializers import (
    OrganizationSerializer, OrganizationMembershipSerializer,
    ProjectSerializer, SprintSerializer, TaskSerializer, CommentSerializer
)


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizationMembershipViewSet(viewsets.ModelViewSet. queryset = OrganizationMembership.objects.all()
    serializer_class = OrganizationMembershipSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        org_slug = self.request.query_params.get('org_slug')
        if org_slug:
            queryset = queryset.filter(organization__slug=org_slug)
        return queryset

class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        project_id = self.request.query_params.get('project_id')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# --- HTMX / HTML Frontend Views with Tenant Scoping ---
class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizations'] = Organization.objects.all()
        context['projects'] = Project.objects.all()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Project, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.all()
        context['status_choices'] = Task.Status.choices
        return context


def create_task(request, pk):
    """HTMX endpoint to securely create a task inside the scoped project."""
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        priority = request.POST.get('priority', Task.Priority.MEDIUM)
        
        if title:
            Task.objects.create(
                project=project,
                title=title,
                description=description,
                priority=priority,
                status=Task.Status.BACKLOG
            )
            
    return render(request, 'partials/task_list.html', {'project': project, 'tasks': project.tasks.all()})