from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
import joblib
# Create your models here.

class MLModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    upload = models.FileField()
    accuracy = models.DecimalField(decimal_places=3, max_digits=5)
    factor = models.DecimalField(decimal_places=3, max_digits=5, null=True)
    noise = models.DecimalField(decimal_places=3, max_digits=5, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.upload) + ' created at ' + str(self.published)

    def predict(self, x, y):
        model = joblib.load(self.upload)
        return model.predict([[x,y]])[0]

    def get_absolute_url(self):
        return reverse('machinelearning:list')