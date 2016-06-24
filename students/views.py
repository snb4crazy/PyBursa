from django.shortcuts import render

from students.models import Student


def list_view(request):
    students_list = []
    student_info = {}

    if request.GET:
        course_id = request.GET['course_id']
        students_set = Student.objects.filter(courses=course_id)
    else:
        students_set = Student.objects.all()
    for student in students_set:
        student_info['id'] = student.id
        student_info['full_name'] = student.surname + ' ' + student.name
        student_info['address'] = student.address
        student_info['skype'] = student.skype
        student_info['courses'] = student.courses.all()
        students_list.append(student_info)
        student_info = {}
    return render(request, 'students/list.html', {'students_list': students_list})


def detail(request, id):
    student = Student.objects.get(id=id)
    student_courses = student.courses.all()
    return render(request, 'students/detail.html', {'student': student, 'courses': student_courses})
