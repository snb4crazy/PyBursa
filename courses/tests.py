from django.test import TestCase, Client
from django.contrib.auth.models import User
from courses.models import Course, Lesson
from coaches.models import Coach
from inspect import getmembers
from pprint import pprint


def create_course():
    return Course.objects.create(name="CourseTest",
                                 short_description="TEST test")


def create_user():
    return User.objects.create(id=1,
                               username="Test",
                               email="test@mail.com")


def create_coach():
    userCoach = create_user()
    return Coach.objects.create(user=userCoach,
                                date_of_birth="1989-01-01",
                                phone="+3807",
                                address="test",
                                skype="test",
                                gender='M',
                                description="Test")


def create_lesson(id):
    return Lesson.objects.create(subject="Test Lesson",
                                 description="test lesson",
                                 course=id,
                                 order=2)


client = Client()


class CoursesListTest(TestCase):

    def test_list_course(self):
        response = client.get('')
        self.assertEqual(response.status_code, 200)

    def test_course_create(self):
        create_course()
        self.assertEqual(Course.objects.all().count(), 1)

    def test_head(self):
        client = Client()
        response = client.get('')
        self.assertContains(response, u'Courses List')

    def test_use_rend(self):
        response = client.get('')
        self.assertTemplateUsed(response, 'base.html')

    def test_html_active(self):
        response = client.get('')
        #pprint(getmembers(response))
        self.assertContains(response, """<h2>Pick The Course</h2>""", html=True)


class CoursesDetailTest(TestCase):

    def test_detail_course(self):
        create_course()
        response = client.get('/courses/2/')
        self.assertEqual(response.status_code, 200)

    def test_create_coach(self):
        create_coach()
        self.assertEqual(Coach.objects.all().count(), 1)

    def test_title_course(self):
        create_course()
        title = Course.objects.get(id=5).name
        response = client.get('/courses/5/')
        self.assertContains(response, title)

    def test_create_lesson(self):
        create_course()
        create_lesson(Course.objects.get(id=1))
        self.assertEqual(Lesson.objects.all().count(), 1)

    def test_list_lesson(self):
        create_course()
        create_course()
        create_lesson(Course.objects.get(id=4))
        create_lesson(Course.objects.get(id=4))
        create_lesson(Course.objects.get(id=3))
        self.assertEqual(Lesson.objects.all().filter(course=4).count(), 2)
