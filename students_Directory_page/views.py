from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . models import StudentCard, course
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
    return render(request, 'pages/index.html')
