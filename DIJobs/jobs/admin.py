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

admin.site.register(Category)
admin.site.register(Job)