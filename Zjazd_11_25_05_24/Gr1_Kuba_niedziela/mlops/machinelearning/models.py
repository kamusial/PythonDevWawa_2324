from django.db import models
from django.contrib.auth.models import User
import datetime
import joblib
# Create your models here.

class MLModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    upload = models.FileField()
    accuracy = models.DecimalField(decimal_places=3, max_digits=5)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField(default=datetime.now)
