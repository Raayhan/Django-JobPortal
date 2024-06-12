from rest_framework import serializers
from .models import Application
from django.contrib.auth.models import User
from .models import Application, Job
import os

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id','title','deadline','company','location','get_absolute_url',]

class ApplicationSerializer(serializers.ModelSerializer):
    candidate = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)
    candidate_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='candidate', write_only=True)
    job_id = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all(), source='job', write_only=True)

    class Meta:
        model = Application
        fields = ('id', 'candidate', 'candidate_id', 'job', 'job_id', 'name', 'email', 'phone', 'cv', 'expected_salary', 'notes', 'status', 'created_at')
        read_only_fields = ('candidate', 'job', 'status', 'created_at')
       
    def create(self, validated_data):
        # Get the current user's first name and last name
        current_user_first_name = self.context['request'].user.first_name
        current_user_last_name = self.context['request'].user.last_name

        # Get the uploaded filename and extension
        uploaded_filename, ext = os.path.splitext(validated_data['cv'].name)

        # Construct the new filename with user's first name and last name merged
        new_filename = f"{current_user_first_name}_{current_user_last_name}{ext}"

        # Set the filename of the cv field to the new filename
        validated_data['cv'].name = new_filename

        # Create the Application instance
        return super().create(validated_data)