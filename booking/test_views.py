from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course, Review, Booking, Timetable
import pytz
import datetime


class TestViews(TestCase):

    # set up test course, review, timetable and booking
    @classmethod
    def setUpTestData(self):

        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.course = Course.objects.create(
                title='test course 1',
                slug='test-course-slug-1',
                skill_level=0,
                duration_in_hrs=2,
                price_in_gbp=50,
                content='this is the test course 1 content',
        )
        self.review = Review.objects.create(
            course=self.course,
            user=self.user,
            written_review='this is a review for course 1'
        )
        self.timetable = Timetable.objects.create(
            course=self.course,
            starts=datetime.datetime(2020, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
        )
        self.booking = Booking.objects.create(
            course=self.timetable,
            user=self.user,
            places_reserved=1
        )

    # retrieve home page and check correct templates are used
    def test_get_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html',
                                'index.html')

    # retrieve course detail page and check correct templates are used
    def test_get_course_detail_page(self):
        response = self.client.get(
                    reverse('course_detail', args=[self.course.slug]))
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'base.html', 'course_detail.html')

    # retrieve booking portal page and check correct templates are used
    def test_get_mybookings_page(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('course_mybookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html',
                                'course_mybookings.html')

    # verify that user can review on course
    def test_can_review_on_course(self):
        self.client.login(user='testuser', password='12345')
        response = self.client.post(
                    reverse('course_detail', args=[self.course.slug]),
                    data={'message': 'new review'})

    # verify that user can book a course
    def test_can_book_a_course(self):
        self.client.login(user='testuser', password='12345')
        response = self.client.post(
                    reverse('course_book'),
                    data={'places_reserved': '1', 'timetable_id': '1'})

    # verify staff user can add course
    def test_get_course_add(self):
        self.client.login(user='testuser', password='1234')
        response = self.client.get('/course/add/')
        self.assertEqual(response.status_code, 302)

    # verify staff user can edit course
    def test_get_course_edit(self):
        self.client.login(user='testuser', password='1234')
        response = self.client.get(
            reverse('course_edit', args=[self.course.slug]))
        self.assertEqual(response.status_code, 302)
