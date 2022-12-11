from django.contrib import admin
from django.urls import include, path

from backend.views import (GetAllCompanies, GetAllProjects, GetAllStudents,
                           GetOneCompany, GetOneProject, GetOneStudent)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/<slug:id>/', GetOneProject.as_view()),
    path('projects/', GetAllProjects.as_view()),
    path('student/<slug:id>/', GetOneStudent.as_view()),
    path('students/', GetAllStudents.as_view()),
    path('company/<slug:id>/', GetOneCompany.as_view()),
    path('companies/', GetAllCompanies.as_view()),
    path('api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),
]
