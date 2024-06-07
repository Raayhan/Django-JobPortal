from django.urls import path,include
from jobs import views

urlpatterns = [

    path('latest-jobs',views.LatestJobsList.as_view()),
    path('jobs/<slug:category_slug>/',views.CategoryDetail.as_view())
   
    
]