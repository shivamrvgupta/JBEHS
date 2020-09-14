from students.forms import StudentRegistration, StudentDetailsForm, StudentPhoto
from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib import auth, messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from results.models import Result, Student
from students.models import StudentDetail, Photo

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def page_not_found(request):
    return render(request, 'pages/404.html')


def addmissionform(request):
    if request.method == 'POST':

        form = StudentRegistration(request.POST)
        if form.is_valid():
            student_code = form.cleaned_data['student_code']
            email = form.cleaned_data['email']
            if Student.objects.filter(student_code=student_code).exists():
                messages.error(request, 'Student code already registered')
                return redirect('admission')
            else:
                form.save()
                return redirect('student_detail')
    else:
        form = StudentRegistration()
    user = Student.objects.all()
    return render(request, 'pages/studentregisteration.html', {'form': form, 'user': user})


def detail_form(request):
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST)
        if form.is_valid():
            student_code = form.cleaned_data['student_code']
            if StudentDetail.objects.filter(student_code=student_code).exists():
                messages.error(request, 'Student code already registered')
                return redirect('student_detail')
                if StudentDetailsForm.objects.filter(student_aadhar_number=student_aadhar_number).exists():
                    messages.error(request, 'Aadhar number already registered')
                    return redirect('student_detail')
            else:
                form.save()
                return redirect('addphoto')
    else:
        form = StudentDetailsForm()
    user = Student.objects.all()
    return render(request, 'pages/studentdetailform.html', {'form': form, 'user': user})


def addphoto(request):
    if request.method == 'POST':
        form = StudentPhoto(request.POST)
        fullname = request.POST['fullname']
        photo = Photo(fullname=fullname)
        photo.save()
        student = Student()
        html_template = "We have got your form and will reach you soon"
        send_mail(
            'Thanks For',
            'Hello, ' + photo.fullname +
            html_template,
            'shivamrvgupta@gmail.com',
            [student.email],
            fail_silently=False,
        )
        if form.is_valid():
            form.save()
        return redirect('admission')
        messages.SUCCESS(request, 'Your form has been submitted')
    else:
        form = StudentPhoto()
    user = Student.objects.all()
    return render(request, 'pages/addphoto.html', {'form': form})
