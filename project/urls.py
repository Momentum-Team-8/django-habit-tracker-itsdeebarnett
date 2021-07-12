"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django import urls
from django.urls import include, path
from django.urls.resolvers import URLPattern
from core import views as habit_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', habit_views.home, name="home"),
    path('accounts/', include('registration.backends.default.urls')),
    path('profile/', habit_views.profile_page, name='profile_page'),
    path('<int:pk>/delete_habit/', habit_views.delete_habit, name='delete_habit'),
    path('<int:pk>/edit_habit/', habit_views.edit_habit, name='edit_habit'),
    path('habits/', habit_views.habit_list, name='habit_list'),
    path('habits/add/', habit_views.add_habit, name='add_habit'),
    path('habits/<int:pk>/trackerlist', habit_views.trackerlist, name='trackerlist')

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
