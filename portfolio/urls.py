from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage with projects, skills, about, and contact form
]
