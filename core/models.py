from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import constraints
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.db.models.constraints import UniqueConstraint

class User(AbstractUser):
    def __str__(self):
        return self.username


class Habit(models.Model):

        user = models.ForeignKey(to=User,on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        goal = models.PositiveIntegerField()
        goaltype = models.CharField(max_length=100, null=True)
        created_date = models.DateTimeField(default=timezone.now)
	
        def __str__(self):
            return self.title


class HabitTracker(models.Model):

        habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
        complete_goal = models.PositiveIntegerField()
        date = models.DateField(null=True)

class Meta:
        constraints = [
            UniqueConstraint(fields=['habit', 'date'], name='unique_records')
        ]