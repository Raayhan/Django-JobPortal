from rest_framework.permissions import AllowAny
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Job
from .models import Category
from .serializers import JobSerializer,CategorySerializer


class LatestJobsList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        jobs = Job.objects.all()[0:16]
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    
class CategoryDetail(APIView):
    permission_classes = [AllowAny]
    def get_object(self,category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Job.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
