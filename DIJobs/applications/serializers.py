from rest_framework import serializers
from .models import Application
from django.contrib.auth.models import User
from .models import Application, Job

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id']

class ApplicationSerializer(serializers.ModelSerializer):
    candidate = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)
    candidate_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='candidate', write_only=True)
    job_id = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all(), source='job', write_only=True)

    class Meta:
        model = Application
        fields = ('id', 'candidate', 'candidate_id', 'job', 'job_id', 'name', 'email', 'phone', 'cv', 'expected_salary', 'notes', 'status', 'created_at')
        read_only_fields = ('candidate', 'job', 'status', 'created_at')
       
