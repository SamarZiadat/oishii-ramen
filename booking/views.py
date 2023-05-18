from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Course
from .forms import ReviewForm


class CourseList(generic.ListView):
    """
    Retrieve course summaries and set pagination
    """
    model = Course
    queryset = Course.objects.filter(status=1).order_by('skill_level')
    template_name = 'index.html'
    paginate_by = 6


class CourseDetail(View):

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
            review_form.instance.name = request.user.username
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
