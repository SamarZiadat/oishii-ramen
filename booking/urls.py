from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.CourseList.as_view(), name='home'),
    path('<slug:slug>/', views.CourseDetail.as_view(), name='course_detail'),
    path('book', login_required(views.CourseBook.as_view()), name='course_book'),
    path('bookings', login_required(views.CourseMyBookings.as_view()), name='course_mybookings'),
]
