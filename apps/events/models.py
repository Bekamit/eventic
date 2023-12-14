from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return f"{self.name}"


class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    banner = models.ImageField(upload_to='media/', null=True, blank=True)
    language = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.title} '


class EventDay(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # week_day = models.CharField(max_length=50, choices=)
