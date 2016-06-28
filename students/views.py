from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
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


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context

    def form_valid(self, form):
        app = form.save()
        messages.success(self.request, "Student %s has been successfully added." % app.full_name())
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request,"Info on the student has been sucessfully changed.")
        return super(StudentUpdateView, self).form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Student info suppression"
        return context

    def form_valid(self, form):
        app = Student.objects.get(self.pk)
        messages.success(self.request, "Info on %s has been sucessfully deleted." % app.full_name())
        app = app.delete()
        return super(StudentDeleteView, self).form_valid(form)