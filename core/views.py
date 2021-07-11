
from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit, Tracker, User
from .forms import HabitForm
from .forms import Habit_trackerForm
from django.contrib.auth.decorators import login_required
from django.utils import timeezone



# Create your views here.
def home(request):
    return render(request, "habit_tracker/home.html")

@login_required
def profile_page(request):
    return render(request, "habit_tracker/profile_page.html")

@login_required
def habit_list(request):
    habit = Habit.objects.all()
    return render(request, "habit_tracker/habit_list.html", {"habit": habit})

def add_habit(request, pk):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.created_date = timezone.now()
            habit.save()
            return redirect('habit_list', pk=pk)
    else:
        form = HabitForm()
    return render(request, 'habit_tracker/add_habit.html', {'form': form})


