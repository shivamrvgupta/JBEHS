from django.shortcuts import render, redirect, HttpResponseRedirect,  get_object_or_404
from django.contrib import messages
from .forms import SchoolRegistration, SchoolUpdate
from .models import School
from django.contrib.auth.decorators import login_required
# Create your views here.

"""
School Operations
"""


@login_required(login_url='/accounts/login/')
def school_registeration(request):
    if request.method == 'POST':
        form = SchoolRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            school_code = form.cleaned_data['school_code']
            if School.objects.filter(school_code=school_code).exists():
                messages.error(request, 'Student code already registered')
                return redirect('add_school')
            else:
                form.save()
                return redirect('show_school')
    else:
        form = SchoolRegistration()
    school = School.objects.all()
    return render(request, 'school/add.html', {'form': form, 'school': school})


@login_required(login_url='/accounts/login/')
def update_data(request, id):
    if request.method == 'POST':
        school = School.objects.get(pk=id)
        form = SchoolUpdate(request.POST, instance=school)
        print('user --- {}'.format(school))
        if form.is_valid():
            form.save()
            print('valid --- {}'.format(form.is_valid))
            return redirect('show_school')
        else:
            print('invalid')
            return redirect('update_school')
        print("didn't enter ")
    else:
        school = School.objects.get(pk=id)
    form = SchoolUpdate(instance=school)
    return render(request, 'school/update.html', {'form': form, 'school': school})


@login_required(login_url='/accounts/login/')
def show_school(request):
    school = School.objects.all()
    return render(request, 'school/show.html', {'school': school})


@login_required(login_url='/accounts/login/')
def delete_data(request, id):
    if request.method == 'POST':
        user = School.objects.get(pk=id)
        user.delete()
        return HttpResponseRedirect('/')


def view(request, id):
    school = get_object_or_404(School, pk=id)

    context = {
        'school': school
    }
    return render(request, 'school/view.html', context)
