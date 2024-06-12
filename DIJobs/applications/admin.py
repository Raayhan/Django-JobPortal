from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
  list_display = ("name", "job","status","expected_salary", "created_at",)
admin.site.register(Application,ApplicationAdmin)
