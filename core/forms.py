from django import forms
from .models import Habit, HabitTracker


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'title',
            'goal',
            'created_date',
        ]


class Habit_trackerForm(forms.ModelForm):
        class Meta:
            Model = HabitTracker
            fields =[
                'habit',
                'complete_goal',
                'date',
            ]