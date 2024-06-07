from rest_framework import serializers

from .models import Category, Job

class JobSerializer(serializers.ModelSerializer):

    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Job
        fields = (
            "id",
            "title",
            "category_name",
            "get_absolute_url",
            "description",
            "salary",
            "date_added",
            "company",
            "experience",
            "location",
            "deadline"
            
        )
    def get_category_name(self, obj):
        return obj.category.name
        
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