from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=30)
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (f'{self.title}-{self.value}')
