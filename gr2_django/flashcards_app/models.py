from django.db import models


class Flashcard(models.Model):
    name = models.CharField(max_length=200)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name
