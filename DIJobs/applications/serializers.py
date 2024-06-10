from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('candidate_id', 'job_id', 'name', 'email', 'phone', 'cv', 'expected_salary', 'notes')
        extra_kwargs = {
            'candidate_id': {'read_only': True},
            'job_id': {'read_only': True},
        }
    
    def validate_phone(self, value):
        if not value.startswith('+88'):
            raise serializers.ValidationError("Phone number must start with +88")
        return value