from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Weekday(models.Model):
    day = models.CharField(max_length = 1000)

    def __str__(self):
        return self.day

class Client(models.Model):
    REPEAT_CHOICES = [
        ("None","None"),
        ("Daily","Daily"),
        ("Weekly","Weekly")
    ]

    SHIFT_CHOICES = [
        ("Morning Shift - 5am to 9am","Morning Shift - 5am to 9am")
    ]
    start_date = models.DateField(auto_now = False)
    arrival_time = models.TimeField(auto_now = False)
    departure_time = models.TimeField(auto_now = False)
    repeat = models.CharField(max_length=100, choices = REPEAT_CHOICES)
    shift_availability = models.CharField(max_length=1000, choices = SHIFT_CHOICES)
    weekdays = models.ManyToManyField(Weekday)
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

