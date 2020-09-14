from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import StudentRegistration, StudentUpdate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student, StudentDetail
# Create your views here.

"""
Students Operations
"""


@login_required(login_url='/accounts/login/')
def index(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            student_code = form.cleaned_data['student_code']
            email = form.cleaned_data['email']
            if Student.objects.filter(student_code=student_code).exists():
                messages.error(request, 'Student code already registered')
                return redirect('add_student')
            else:
                form.save()
                return redirect('show_student')
    else:
        form = StudentRegistration()
    user = Student.objects.all()
    return render(request, 'student/add.html', {'form': form, 'user': user})


@login_required(login_url='/accounts/login/')
def show(request):
    student = Student.objects.all()
    return render(request, 'student/show.html', {'student': student})


@login_required(login_url='/accounts/login/')
def update_data(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentUpdate(request.POST, instance=student)

        if form.is_valid():
            form.save()
            print('VAlid --- {}'.format(form.is_valid))
            return redirect('update_student')
        else:
            print('invalid')
            return redirect('show_student')
        print("didn't enter ")
    else:
        student = Student.objects.get(pk=id)
    form = StudentUpdate(instance=student)
    return render(request, 'student/update.html', {'form': form})


@login_required(login_url='/accounts/login/')
def delete_data(request, id):
    if request.method == 'POST':
        user = Student.objects.get(pk=id)
        user.delete()
        return redirect('/')
