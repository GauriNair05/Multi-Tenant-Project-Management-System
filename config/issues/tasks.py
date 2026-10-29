import time
from celery import shared_task
from .models import Project

@shared_task
def generate_project_report(project_id):
    """
    Simulates a heavy background process, like compiling analytics 
    or generating a PDF report for a project.
    """
    print(f"[{time.strftime('%X')}] Celery Task Started: Processing report for project ID {project_id}...")
    

    time.sleep(5)
    
    try:
        project = Project.objects.get(id=project_id)
        report_result = f"Report generated successfully for project: {project.name} [{project.key}]"
    except Project.DoesNotExist:
        report_result = f"Project with ID {project_id} not found."

    print(f"[{time.strftime('%X')}] Celery Task Completed: {report_result}")
    return report_result