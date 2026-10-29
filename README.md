# Multi-Tenant Project Management System

A production-ready, full-stack multi-tenant project management and issue-tracking platform built with Django, Django REST Framework (DRF), Celery, HTMX, and Tailwind CSS.

## Architecture and Core Features

- **Multi-Tenant Isolation**: Organization-level tenant scoping to secure workspace isolation, ensuring data separation across different organizations.
- **Hybrid Frontend**: Dynamic, single-page application (SPA)-like user experience powered by HTMX and styled with Tailwind CSS, eliminating full page reloads for task creation and updates.
- **REST API Layer**: Comprehensive, secure RESTful API endpoints built using Django REST Framework ViewSets and routers.
- **Asynchronous Processing**: Integrated Celery task queue with a background broker for managing long-running background operations and reporting tasks.
- **Robust Task Tracking**: Support for project keys, custom priorities, statuses, sprints, and inline task creation.

## Tech Stack

- **Backend**: Python, Django, Django REST Framework, Celery
- **Frontend**: HTMX, Tailwind CSS, HTML5, Server-Side Rendering (SSR)
- **Database & Storage**: SQLite, SQL

## Project Structure

```text
issues-tracker-backend/
├── config/                  # Project configuration settings and root URLs
├── issues/                  # Core application (models, views, serializers, tasks)
├── templates/               # HTML templates (Dashboard, Project Detail, Partials)
├── manage.py                # Django management utility
└── db.sqlite3               # SQLite database
