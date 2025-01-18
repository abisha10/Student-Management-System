from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student
from .forms import StudentForm


# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students':students})

#function to view a student, get a particular student by id. Here pk means primary key, it gets a student matches with the id
def view_student(request,id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_stu_num = form.cleaned_data['stu_num']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']

            new_student = Student(
                stu_num = new_stu_num,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa
            )
            new_student.save()
            return render(request, 'add.html', {
                'form': StudentForm(),
                'success' : True
            })
        else:
             return render(request, 'add.html', {
                'form': form,  # Re-render the form with validation errors
                'success': False
            })
    else:
        form = StudentForm()
    return render(request, 'add.html', {
        'form': form,
        'success': False
        
    })
def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'edit.html', {
                'form': form,
                'success' : True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {
                'form': form,
            })

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('indexx:index'))