from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from .models import Course, Booking, Timetable
from .forms import ReviewForm, CourseForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
import datetime
import pytz


class CourseList(generic.ListView):
    """
    Retrieve course summaries and set pagination
    """
    model = Course
    queryset = Course.objects.filter(status=1).order_by('skill_level')
    template_name = 'index.html'
    paginate_by = 6


class CourseDetail(View):
    """
    Display course details for selected hike

    get method : retrieve course details including reviews
                 and render course detail page

    post method : validate review input, store and re-load detail page
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Course.objects.filter(status=1)
        course = get_object_or_404(queryset, slug=slug)
        reviews = course.reviews.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "course_detail.html",
            {
                "course": course,
                "reviews": reviews,
                "reviewed": False,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Course.objects.filter(status=1)
        course = get_object_or_404(queryset, slug=slug)
        reviews = course.reviews.filter(approved=True).order_by("-created_on")

        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.user = request.user
            review = review_form.save(commit=False)
            review.course = course
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "course_detail.html",
            {
                "course": course,
                "reviews": reviews,
                "reviewed": True,
                "review_form": ReviewForm()
            },
        )


class CourseMyBookings(LoginRequiredMixin, View):
    """
    Display booking information for current user

    get method : retrieve past and upcoming bookings for user
                 and render my bookings page

    post method : cancel selected booking and reload page
    """

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(user=self.request.user).filter(
                    course__starts__gt=datetime.datetime.now(
                                        pytz.utc)).order_by('course__starts')
        past_bookings = Booking.objects.filter(
                    user=self.request.user).filter(
                    course__starts__lte=datetime.datetime.now(
                                        pytz.utc)).order_by('course__starts')

        return render(
            request,
            "course_mybookings.html",
            {
                "bookings": bookings,
                "past_bookings": past_bookings,
            }
        )

    def post(self, request, *args, **kwargs):
        id = request.POST.get('cancel_booking_id')
        booking = get_object_or_404(Booking, id=id)
        booking.delete()

        # Used HttpResponseRedirect here instead of render to ensure
        # delete request is not re-submitted on bookings page re-load
        messages.success(request, 'Your booking has been cancelled.')
        return HttpResponseRedirect(reverse('course_mybookings'))


class CourseBook(LoginRequiredMixin, View):
    """
    Book course panel displayed on course detail page

    post method : check input, create new booking for current user
                  for selected timetabled course then redirect to
                  bookings page
    """

    def post(self, request):

        user = request.user
        places_reserved = request.POST.get('places_reserved')
        # validate number of places reserved
        if places_reserved in ['1', '2', '3', '4', '5']:
            timetable_id = request.POST.get('timetable_id')
            timeslot = get_object_or_404(Timetable, id=timetable_id)
            Booking.objects.create(course=timeslot, user=user,
                                   places_reserved=places_reserved)
            messages.success(request, 'Thank you for your booking request!')
            # Used HttpResponseRedirect here instead of render to ensure
            # booking is not re-submitted on bookings page re-load

        return HttpResponseRedirect(reverse('course_mybookings'))


class CourseAdd(LoginRequiredMixin,
                SuccessMessageMixin,
                UserPassesTestMixin,
                generic.CreateView):
    """
    View to allow staff to add a new course
    Success message as user feedback
    """
    model = Course
    template_name = 'course_add.html'
    form_class = CourseForm
    success_message = 'Course added!'

    def form_valid(self, form):
        """Validate form after confirming user is staff"""
        form.instance.is_staff = self.request.user.is_staff
        return super().form_valid(form)

    def test_func(self):
        """Test that logged in user is staff"""
        post = self.get_slug_field()
        if self.request.user.is_staff:
            return True
        return False


class CourseEdit(LoginRequiredMixin,
                 UserPassesTestMixin,
                 SuccessMessageMixin,
                 generic.UpdateView):
    """
    View to allow staff to edit courses
    on the course detail page
    Success message as user feedback
    """
    model = Course
    template_name = 'course_edit.html'
    form_class = CourseForm
    success_message = 'Course updated!'

    def form_valid(self, form):
        """Validate form after confirming user is staff"""
        form.instance.is_staff = self.request.user.is_staff
        return super().form_valid(form)

    def test_func(self):
        """Test that logged in user is staff"""
        post = self.get_object()
        if self.request.user.is_staff:
            return True
        return False


class CourseDelete(LoginRequiredMixin,
                   SuccessMessageMixin,
                   UserPassesTestMixin,
                   generic.DeleteView):
    """
    View to allow staff users to delete course
    on the course detail page
    Success message as user feedback
    """
    model = Course
    template_name = 'course_detail.html'
    success_url = reverse_lazy('home')
    success_message = 'Course deleted.'

    def delete(self, request, *args, **kwargs):
        """Generate success message on delete view"""
        messages.success(self.request, self.success_message)
        return super(CourseDelete, self).delete(request, *args, **kwargs)

    def test_func(self):
        """Test that logged in user is staff"""
        post = self.get_object()
        if self.request.user.is_staff:
            return True
        return False
