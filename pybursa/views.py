from django.shortcuts import render
from courses.models import Course


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_details(request):
    return render(request, 'student_details.html')


def courses_list(request):
    return render(request, 'courses_list.html', {'courses': Course.objects.all()})
