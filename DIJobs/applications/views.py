from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Application, Job
from .serializers import ApplicationSerializer
import os
import logging

logger = logging.getLogger(__name__)
class SubmitApplication(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, category_slug, job_slug):
        try:
            job = Job.objects.get(slug=job_slug, category__slug=category_slug)
        except Job.DoesNotExist:
            
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if not request.user.is_authenticated:
           
            return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        data = request.data.copy()
        data['candidate_id'] = request.user.id
        data['job_id'] = job.id
        data['status'] = 0

        serializer = ApplicationSerializer(data=data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckApplicationStatus(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id, job_id):
        try:
            application = Application.objects.get(candidate_id=user_id, job_id=job_id)
            return Response({"applied": True})
        except Application.DoesNotExist:
            return Response({"applied": False})

class UserApplicationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        
        applications = Application.objects.filter(candidate_id=request.user.id)
       
        serializer = ApplicationSerializer(applications, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class WithdrawApplication(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id, format=None):
        
        try:
            application = Application.objects.get(id=id)
            if application.candidate != request.user:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
            if application.cv:
                cv_path = application.cv.path
                if os.path.exists(cv_path):
                    os.remove(cv_path)
            application.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Application.DoesNotExist:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)