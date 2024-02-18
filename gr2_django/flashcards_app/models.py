from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Flashcard(models.Model):
    name = models.CharField(max_length=200)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=200)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def learn_url(self):
        return reverse("learn-flashcard", args=[self.slug])
