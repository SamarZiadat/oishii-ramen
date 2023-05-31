from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Review, Course, Timetable, Booking
import pytz
import datetime


class TestAdmin(TestCase):

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

    # login as a superuser, use the approve_review action to approve the
    # review created during setup, check the response code returned
    # and check that the review is now approved
    def test_approve_reviews(self):

        User.objects.create_superuser(
            user='super', email='test@example.com', password='54321',
        )
        self.client.login(user='super', password='54321')

        # count how many reviews are currently approved
        approved = Review.objects.filter(approved=True).count()
        self.assertFalse(self.review.approved)

        data = {
            'action': 'approve_reviews',
            '_selected_action': [self.review.id, ]}
        change_url = reverse('admin:booking_review_changelist')
        response = self.client.post(change_url, data, follow=True)

        self.assertEqual(response.status_code, 200)

        # check number of approved reviews has increased by one
        self.assertEqual(
            Review.objects.filter(approved=True).count(), approved+1)

    # login as a superuser, use the approve_booking action to approve the
    # booking created during setup, check the response code returned
    # and check that booking is now approved
    def test_approve_bookings(self):

        User.objects.create_superuser(
            user='super', email='test@example.com', password='54321',
        )
        self.client.login(user='super', password='54321')

        # count how many bookings are currently approved
        approved = Booking.objects.filter(approved=True).count()
        self.assertFalse(self.review.approved)

        data = {
            'action': 'approve_bookings',
            '_selected_action': [self.booking.id, ]}
        change_url = reverse('admin:booking_booking_changelist')
        response = self.client.post(change_url, data, follow=True)

        self.assertEqual(response.status_code, 200)

        # check number of approved bookings has increased by one
        self.assertEqual(
            Booking.objects.filter(approved=True).count(), approved+1)

    # login as a superuser, use the publish_courses action to update status of
    # course created during setup, check the response code returned and
    # check that the course is now status=1 (published)
    def test_publish_courses(self):
        User.objects.create_superuser(
            user='super', email='test@example.com', password='54321',
        )
        self.client.login(user='superstar', password='54321')

        # count how many courses are published
        published = Course.objects.filter(status=1).count()
        self.assertEqual(self.course.status, 0)

        data = {
            'action': 'publish_courses',
            '_selected_action': [self.course.id, ]}
        change_url = reverse('admin:booking_course_changelist')
        response = self.client.post(change_url, data, follow=True)

        self.assertEqual(response.status_code, 200)

        # check number of published courses has increased by one
        self.assertEqual(Course.objects.filter(status=1).count(), published+1)
