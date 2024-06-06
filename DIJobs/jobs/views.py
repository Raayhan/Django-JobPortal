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
        jobs = Job.objects.all()[0:4]
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    

