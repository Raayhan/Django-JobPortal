from rest_framework import serializers

from .models import Category, Job

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "description",
            "salary",
            "date_added",
            
        )
        
class CategorySerializer(serializers.ModelSerializer):

    jobs = JobSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "jobs"
        )