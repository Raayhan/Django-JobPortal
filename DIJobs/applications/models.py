from django.db import models
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from jobs.models import Job

def validate_cv_file(value):
    """
    Validate that the uploaded file is either a PDF or DOC/DOCX.
    """
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Only PDF and DOC/DOCX files are allowed.')


class Application(models.Model):
    candidate       = models.ForeignKey(User,related_name='applications',on_delete=models.CASCADE)
    job             = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)  # ForeignKey to Job model
    name            = models.CharField(max_length=100)
    email           = models.CharField(max_length=100)
    phone           = models.CharField(max_length=14)
    cv              = models.FileField(upload_to='cvs/', validators=[validate_cv_file])
    expected_salary = models.DecimalField(max_digits=8,decimal_places=2)
    notes           = models.CharField(max_length=255)
    status          = models.IntegerField(default=0)
    created_at      = models.DateTimeField(auto_now_add=True)
 

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.name
