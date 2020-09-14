from django.urls import path
from results import views

urlpatterns = [
    path('add/', views.add_result, name='add_results'),
    path("rollnumber/", views.enterrollnumber, name="rollnumber"),
    path('show/', views.show, name='show_result'),
    path('update/<int:id>/', views.update_data, name='update_result'),
    path('delete/<int:id>/', views.delete_data, name='delete_result'),
]
