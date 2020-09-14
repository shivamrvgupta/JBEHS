from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import AddResult, ResultUpdate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Result

# Create your views here.


def index(request, roll_number):
    result = get_object_or_404(Result, pk=roll_number)

    context = {
        'results': result
    }
    return render(request, 'results/result.html', context)


def enterrollnumber(request):
    if request.method == 'POST':
        student_code = request.POST['rollnumber']
        print('RollNumber --- {}'.format(student_code))

        result_query = Result.objects.filter(roll_number=student_code)

        print('result -- {}'.format(result_query))

        if result_query:
            print('valid roll number')
            print('student.id ----- {}'.format(result_query[0].roll_number))
            return redirect('results/' + str(result_query[0].id))
        else:
            print('invalid roll number')
            return redirect('404')

    else:

        return render(request, 'results/enterrollmuber.html')

    return render(request, 'results/enterrollmuber.html')


"""
Result Operations
"""


@login_required(login_url='/accounts/login/')
def add_result(request):
    if request.method == 'POST':
        form = AddResult(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            roll_number = form.cleaned_data['roll_number']
            if Result.objects.filter(roll_number=roll_number).exists():
                messages.error(request, 'Roll Number already registered')
                return redirect('add_results')
            else:
                form.save()
                messages.error(request, 'Registered Successfully')
                return redirect('show_result')
    else:
        form = AddResult()
    result = Result.objects.all()
    return render(request, 'results/add.html', {'form': form, 'result': result})


@login_required(login_url='/accounts/login/')
def update_data(request, id):
    if request.method == 'POST':
        result = Result.objects.get(pk=id)
        form = ResultUpdate(request.POST, instance=result)
        print('user --- {}'.format(result))
        if form.is_valid():
            form.save()
            print('valid --- {}'.format(form.is_valid))
            return redirect('show_result')
        else:
            print('invalid')
            return redirect('update_result')
        print("didn't enter ")
    else:
        result = Result.objects.get(pk=id)
        results = Result.objects.all()
    form = ResultUpdate(instance=result)
    return render(request, 'results/update.html', {'form': form, 'results': results})


@login_required(login_url='/accounts/login/')
def show(request):
    result = Result.objects.all()
    return render(request, 'results/show.html', {'result': result})


@login_required(login_url='/accounts/login/')
def delete_data(request, id):
    if request.method == 'POST':
        result = Result.objects.get(pk=id)
        result.delete()
        return HttpResponseRedirect('/')
