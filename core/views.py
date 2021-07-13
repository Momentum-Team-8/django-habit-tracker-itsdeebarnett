
from django.shortcuts import render, get_object_or_404, redirect
from .models import Habit, HabitTracker
from .forms import HabitForm, Habit_trackerForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone



# Create your views here.
def home(request):
    return render(request, "habit_tracker/home.html")

@login_required
def profile_page(request):
    return render(request, "habit_tracker/profile_page.html")

@login_required
def habit_list(request):
    habits = Habit.objects.all()
    return render(request, "habit_tracker/habit_list.html", {"habits": habits})


def trackerlist(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    tracker = habit.tracker.filter()
    return render(request, "habit_tracker/trackerlist.html", {"habit":habit, "tracker":tracker, "pk": pk})

@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.created_date = timezone.now()
            habit.save()
            return redirect(to='habit_list')
    else:
        form = HabitForm()
    return render(request, 'habit_tracker/add_habit.html', {'form': form})

@login_required
def edit_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.created_date = timezone.now()
            habit.save()
            return redirect('habit_list')
    else:
        form = HabitForm()
    return render(request, 'habit_tracker/add_habit.html', {'form': form})


def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    if request.method == 'POST':
        habit.delete()
        return redirect('habit_list')
    return render(request, 'habit_tracker/delete_habit.html', {'habit': habit})

