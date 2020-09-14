from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addmisionform", views.addmissionform, name="admission"),
    path("detailform", views.detail_form, name="student_detail"),
    path("addphoto", views.addphoto, name="addphoto"),
    path("404/", views.page_not_found, name="404"),

]
