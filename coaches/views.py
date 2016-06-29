from django.shortcuts import render
from coaches.models import Coach


def detail(request, coach_id):
    coach = Coach.objects.get(id=coach_id)
    coach_course = coach.coach_courses.all()
    assist_courses = coach.assistant_courses.all()
    return render(request, 'coaches/detail.html', {'coach': coach, 'courses': coach_course, 'assist_courses': assist_courses})
