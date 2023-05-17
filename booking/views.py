from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Course


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
                "reviews": reviews
            },
        )
