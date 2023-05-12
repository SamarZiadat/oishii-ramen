from django.contrib import admin
from .models import Course
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('skill_level', 'location')
    summernote_fields = ('content')
