from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . models import StudentCard, course

from NewUserRegistrationForm.models import Register
# Create your views here.
def index(request):
    student = StudentCard.objects.all() # stroing all the data from the database into student varibale
    #filter by Name
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            student=student.filter(Name__iexact=keyword)
    #used for searching by courseName
    if 'selectspec' in request.GET:
        spec= request.GET['selectspec']
        if spec== 'FirstYear':
            student = student.filter(acadamicYear__iexact=spec)
        elif spec =='ALL':
            student = StudentCard.objects.all()
        elif spec == 'SecondYear':
            student = student.filter(acadamicYear__iexact=spec)
        elif spec == 'Passed_out':
            student = student.filter(acadamicYear__iexact=spec)
        else:
            student= student.filter(specalization__iexact=spec)
    context={
        'student':student
    }
    return render(request, 'pages/index.html', context)


def student(request, student_id):
    # storing all the data in the variable
    data = course.objects.all()
    filterData = data.filter(studentKey__id=student_id)
    profile = StudentCard.objects.all().filter(id=student_id)
    print(profile,"*******************")
    context ={
        'studentData':filterData,
        'profile':profile
    }
    return render(request, 'pages/studentDetails.html', context)
