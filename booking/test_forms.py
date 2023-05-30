from django.test import TestCase
from .forms import ReviewForm, CourseForm


class TestReviewForm(TestCase):

    # test that message value needs to be provided
    def test_message_is_required(self):
        form = ReviewForm({'message': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')

    # test that message is named as an explicit field
    def test_fields_are_explicit_in_forms_metaclass(self):
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ('message',))

class TestCourseForm(TestCase):

    # test that title field is required
    def test_course_title_is_required(self):
        form = CourseForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    # test that skill level field is required 
    def test_course_skill_level_is_required(self):
        form = CourseForm({'skill_level': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('skill_level', form.errors.keys())
        self.assertEqual(form.errors['skill_level'][0], 'This field is required.')
    
    # test that duration field is required 
    def test_course_duration_in_hrs_is_required(self):
        form = CourseForm({'duration_in_hrs': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('duration_in_hrs', form.errors.keys())
        self.assertEqual(form.errors['duration_in_hrs'][0],
                         'This field is required.')

    # test that price field is required 
    def test_course_price_in_gbp_is_required(self):
        form = CourseForm({'price_in_gbpprice_in_gbp': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price_in_gbp', form.errors.keys())
        self.assertEqual(form.errors['price_in_gbp'][0],
                         'This field is required.')

    # test that content field is required 
    def test_post_content_is_required(self):
        form = CourseForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    # test that fields are explicit in course metaclass
    def test_fields_are_explicit_in_post_metaclass(self):
        form = CourseForm()
        self.assertEqual(form.Meta.fields, ['title', 'skill_level', 'duation_in_hrs',
                         'price_in_gbp', 'featured_image', 'content'])