from django.contrib import admin
from .models import Category,Job
from ckeditor.widgets import CKEditorWidget
from django import forms

class JobAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Job
        fields = '__all__'

class JobAdmin(admin.ModelAdmin):
    form = JobAdminForm
    

class JobList(admin.ModelAdmin):
    list_display = ("title","category","company","location","salary","deadline","date_added")

class CategoryList(admin.ModelAdmin):
    list_display = ("name","slug")

    
admin.site.register(Category,CategoryList)
admin.site.register(Job,JobList)