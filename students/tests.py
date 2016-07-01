from django.test import TestCase, Client
from students.models import Student


def create_student():
    return Student.objects.create(name="Test",
                                  surname="Test",
                                  date_of_birth="1989-01-01",
                                  email="test@mail/com",
                                  phone="+3807",
                                  address="test",
                                  skype="test")

client = Client()


class StudentsListTest(TestCase):

    def test_list_student(self):
        response = client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_student_create(self):
        create_student()
        self.assertEqual(Student.objects.all().count(), 1)

    def test_filter_course(self):
        course_id = 1
        response = self.client.get('/students/', {'course_id': course_id})
        std_filter = Student.objects.filter(courses__pk=course_id).all()
        for std in response.context['object_list'].all():
            self.assertIn(std, std_filter)

    def test_use_rend(self):
        response = client.get('')
        self.assertTemplateUsed(response, 'base.html')

    def test_nav_active(self):
        response = client.get('/students/')
        self.assertContains(response, """<li class=active><a href="/students/">Students</a></li>""", html=True)


class StudentsDetailTest(TestCase):

    def test_detail_student(self):
        create_student()
        response = client.get('/students/1/')
        self.assertEqual(response.status_code, 200)

    def test_head(self):
        create_student()
        title = Student.objects.get(id=1).full_name()
        response = client.get('/students/1/')
        self.assertContains(response, title)

    def test_ans(self):
        create_student()
        response = client.get('/students/1')
        self.assertEqual(response.status_code, 301)

    def test_temp_name(self):
        create_student()
        response = client.get('/students/1/')
        self.assertTemplateUsed(response, 'students/student_detail.html')

    def test_error(self):
        response = client.get('/students/2/')
        self.assertEqual(response.status_code, 404)
