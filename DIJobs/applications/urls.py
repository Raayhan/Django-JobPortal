from django.urls import path,include
from applications import views

from .views import SubmitApplication
from .views import CheckApplicationStatus

urlpatterns = [
    
    path('jobs/<slug:category_slug>/<slug:job_slug>/apply', SubmitApplication.as_view()),
    path('applications/check/<int:user_id>/<int:job_id>/', CheckApplicationStatus.as_view())
]