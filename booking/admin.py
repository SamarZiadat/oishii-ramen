from django.contrib import admin
from .models import Course
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
