from django.contrib import admin
from django.urls import path

from backend.views import ServerConnect

urlpatterns = [
    path('admin/', admin.site.urls),  # Need to comment it before migrations
    path('hello/', ServerConnect.as_view())
]
