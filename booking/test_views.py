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

        self.user = User.objects.create(user='testuser')
        self.user.set_password('12345')
        self.user.save()

        self.course = Course.objects.create(
                title='test course 1',
                slug='test-course-slug-1',
                skill_level=0,
                duration_in_hrs=2,
                price_in_ggbp=50,
                content='this is the test course 1 content',
        )
        self.review = Review.objects.create(
            course=self.course,
            usere=self.user,
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
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'navigation.html')
        self.assertTemplateUsed(response, 'footer.html')
        self.assertTemplateUsed(response, 'index.html')

    # retrieve course detail page and check correct templates are used
    def test_get_course_detail_page(self):
        response = self.client.get(
                    reverse('course_detail', args=[self.course.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'navigation.html')
        self.assertTemplateUsed(response, 'footer.html')
        self.assertTemplateUsed(response, 'index.html')

    # retrieve booking portal page and check correct templates are used
    def test_get_mybookings_page(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('course_mybookings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'course_mybookings.html')
        self.assertTemplateUsed(response, 'navigation.html')
        self.assertTemplateUsed(response, 'footer.html')

    # verify that user can review on course and page is refreshed
    def test_can_comment_on_course(self):
        self.client.login(user='testuser', password='12345')
        response = self.client.post(
                    reverse('course_detail', args=[self.hcourse.slug]),
                    data={'message': 'new review'})
        self.assertRedirects(
            response, reverse('course_detail', args=[self.course.slug]))

    # verify that user can book a course and is brought to booking portal page
    def test_can_book_a_course(self):
        self.client.login(user='testuser', password='12345')
        response = self.client.post(
                    reverse('course_book'),
                    data={'places_reserved': '1', 'timetable_id': '1'})
        self.assertRedirects(response, reverse('course_mybookings'))

    # verify user can cancel booking and that page is refreshed
    def test_can_cancel_booking(self):
        self.client.login(user='testuser', password='12345')
        booking = Booking.objects.create(
            course=self.timetable,
            user=self.user,
            places_reserved=1
        )
        matching_bookings = Booking.objects.filter(id=booking.id)
        self.assertEqual(len(matching_bookings), 1)
        response = self.client.post(
                    reverse('course_mybookings'),
                    data={'cancel_booking_id': f'{booking.id}'})
        self.assertRedirects(response, reverse('course_mybookings'))
        matching_bookings = Booking.objects.filter(id=booking.id)
        self.assertEqual(len(matching_bookings), 0)
