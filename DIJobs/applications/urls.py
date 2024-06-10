from django.urls import path,include
from applications import views

from .views import SubmitApplication

urlpatterns = [
    
    path('jobs/apply/<int:job_id>/', SubmitApplication.as_view()),
]