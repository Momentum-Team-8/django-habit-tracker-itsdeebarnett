from django import forms
from .models import Habit, Tracker


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'user'
            'title'
            'goals'
            'created_date',
        ]


class Habit_trackerForm(forms.ModelForm):
        class Meta:
            Model = Tracker
            fields =[
                'habit'
                'complete_goal'
                'date'
            ]