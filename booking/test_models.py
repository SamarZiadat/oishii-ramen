from django.test import TestCase
from .models import Course, Review, Timetable, Booking
import pytz
import datetime
from unittest import mock
from django.contrib.auth.models import User


class TestModels(TestCase):

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

    # test the __str__ method for Course
    def test_course_str(self):
        self.assertEqual(str(self.course), 'test course 1')

    # test default values working as expected
    # for Course status and image fields
    def test_course_defaults(self):
        self.assertEqual(self.course.status, 0)
        self.assertEqual(self.course.featured_image, 'placeholder')

    # test default values working as expected for Course date fields
    def test_course_dates_default(self):
        mocked = datetime.datetime(2018, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now',
                        mock.Mock(return_value=mocked)):
            hike = Course.objects.create(
                title='test course 2',
                slug='test-course-slug-2',
                skill_level=0,
                duration_in_hrs=2,
                price_in_gbp=50,
                content='this is the test course 2 content',
            )

    # test the __str__ method for Review
    def test_review_str(self):
        self.assertEqual(
            str(self.review),
            f'Review this is a review for course 1 by {self.user.username}')

    # test default value working as expected for Review approved field
    def test_review_approved_default(self):
        self.assertFalse(self.review.approved)

    # test default values working as expected for Review date field
    def test_review_date_default(self):
        mocked = datetime.datetime(2018, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
        with mock.patch('django.utils.timezone.now',
                        mock.Mock(return_value=mocked)):
            review = Review.objects.create(
                 course=self.course,
                 user=self.user,
                 written_review='this is another review for course 1'
            )
            self.assertEqual(review.created_on, mocked)

    # test default value working as expected for Booking approved field
    def test_booking_approved_default(self):
        self.assertFalse(self.booking.approved)
