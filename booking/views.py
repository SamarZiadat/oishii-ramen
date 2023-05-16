from django.shortcuts import render
from django.views import generic
from models import Course


class CourseList(generic.ListView):
    """
    Retrieve course summaries and set pagination
    """
    model = Course
    queryset = Course.objects.filter(status=1).order_by('skill_level')
    template_name = 'index.html'
    paginate_by = 6
