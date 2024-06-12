from django.urls import path,include
from applications import views

from .views import SubmitApplication

urlpatterns = [
    
    path('jobs/<slug:category_slug>/<slug:job_slug>/apply', SubmitApplication.as_view()),
]