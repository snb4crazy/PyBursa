from django.shortcuts import render
from courses.models import Course


def index(request):
    courses = Course.objects.only('name', 'short_description', 'id')
    return render(request, 'index.html', {"courses": courses})


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_details(request):
    return render(request, 'student_details.html')


def courses_list(request):
    return render(request, 'courses_list.html', {'courses': Course.objects.all()})
