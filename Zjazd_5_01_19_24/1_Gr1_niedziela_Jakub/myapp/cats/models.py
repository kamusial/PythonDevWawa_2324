from django.db import models

# Create your models here.

"""
{
        "user": "58e007480aac31001185ecef",
        "text": "When asked if her husband had any hobbies, Mary Todd Lincoln is said to have replied \"cats.\"",
        "source": "user",
        "createdAt": "2018-02-19T21:20:03.434Z",
        "updatedAt": "2020-08-23T20:20:01.611Z",
        "type": "cat",
        "deleted": false,
        "used": false
    }
"""


class CatsFact(models.Model):
    fact_owner = models.CharField(max_length=255)
    text = models.TextField(max_length=1000)
    source = models.CharField(max_length=255)
    createdAt = models.CharField(max_length=255)
    updatedAt = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    deleted = models.BooleanField()
    used = models.BooleanField()