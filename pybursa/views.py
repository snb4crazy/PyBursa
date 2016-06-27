from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_details(request):
    return render(request, 'student_details.html')


def courses_list(request):
    return render(request, 'courses_list.html')
