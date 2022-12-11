from django.contrib import admin
from django.urls import path, include

from backend.views import GetOneProject, GetAllProjects


urlpatterns = [
    path('admin/', admin.site.urls),  # Need to comment it before migrations
    path('project/<slug:id>/', GetOneProject.as_view()),
    path('projects/', GetAllProjects.as_view()),
    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),
]
