from django.shortcuts import render

from courses.models import Course, Lesson


def detail(request, id):
    course = Course.objects.get(id=id)
    lessons = Lesson.objects.filter(course_id=id)
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons, 'id': id})


def index(request):
    courses = Course.objects.only('name', 'short_description', 'id')
    return render(request, 'index.html', {"courses": courses})
