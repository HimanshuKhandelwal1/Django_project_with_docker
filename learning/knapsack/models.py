from django.db import models

# Create your models here.

class knaps(models.Model):
    weights = models.CharField(max_length=255, null=False)
    matix = models.CharField(max_length=255, null=False)
    Attachment = models.FileField()

