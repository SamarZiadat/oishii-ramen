from django.contrib import admin
from .models import Course, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'skill_level', 'location')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('skill_level', 'location')
    summernote_fields = ('content')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('written_review', 'course', 'username', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('username', 'written_review')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)
