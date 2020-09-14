from django.urls import path
from . import views

urlpatterns = [
    # School
    path('add/', views.school_registeration, name='add_school'),
    path('update/<int:id>/', views.update_data, name='update_school'),
    path('show/', views.show_school, name='show_school'),
    path('show/<int:id>/', views.view, name='view'),
    path('delete/<int:id>/', views.delete_data, name='delete_school'),
]
