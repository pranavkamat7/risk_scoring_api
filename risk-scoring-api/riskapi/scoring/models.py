from django.db import models

# Create your models here.
class RiskAssessment(models.Model):
    purpose = models.CharField(max_length=100)
    data_sensitivity = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    processor_name = models.CharField(max_length=100)
    risk_score = models.IntegerField(null=True, blank=True)
    risk_breakdown = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)