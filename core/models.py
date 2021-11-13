from django.db import models


# Create your models here.
class TaxQueue(models.Model):
    kra_pin = models.CharField(max_length=20, null=True, blank=True)
    filed = models.BooleanField(default=False)
    
