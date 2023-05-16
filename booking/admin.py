from django.contrib import admin
from .models import Course, Review, Timetable, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'skill_level')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('skill_level', 'duration', 'price')
    summernote_fields = ('content')
    actions = ['publish_course']

    def publish_course(self, request, queryset):
        queryset.update(status=1)


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('written_review', 'course', 'username', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('username', 'written_review')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('course', 'starts')
    list_filter = ('course', 'starts')
    search_fields = ('course__title', 'starts')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('course', 'username', 'places_reserved', 'approved')
    list_filter = ('course', 'username__username', 'approved')
    search_fields = ('course__course__title', 'username__username')
    actions = ['approve_bookings']

    def approve_bookings(self, request, queryset):
        queryset.update(approved=True)
