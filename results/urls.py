from django.urls import path
from . import views

urlpatterns = [
    path('results/<str:roll_number>/', views.index, name="results"),
]
