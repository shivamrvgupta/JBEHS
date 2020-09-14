from django.urls import path
from . import views

urlpatterns = [
    # Student
    path('add/', views.index, name='add_student'),
    path('show/', views.show, name='show_student'),
    path('update/<int:id>/', views.update_data, name='update_student'),
    path('delete/<int:id>/', views.delete_data, name='delete_student'),
]
