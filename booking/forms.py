from .models import Review, Course
from django import forms
from django_summernote.widgets import SummernoteWidget


class ReviewForm(forms.ModelForm):
    """
    Form for reviews
    """
    class Meta:
        model = Review
        fields = ('written_review',)


class CourseForm(forms.ModelForm):
    """
    Form for courses
    """
    class Meta:
        """Form fields"""
        model = Course
        fields = [
            'title',
            'skill_level',
            'duration_in_hrs',
            'price_in_gbp',
            'content',
            'featured_image'
        ]
        widgets = {
            'content': SummernoteWidget(),
        }
