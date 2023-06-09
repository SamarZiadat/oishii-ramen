from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
               path('', views.CourseList.as_view(), name='home'),
               path('<slug:slug>/course-detail/',
                    views.CourseDetail.as_view(), name='course_detail'),
               path('book', login_required(views.CourseBook.as_view()),
                    name='course_book'),
               path('bookings',
                    login_required(views.CourseMyBookings.as_view()),
                    name='course_mybookings'),
               path('course/add/', views.CourseAdd.as_view(),
                    name='course_add'),
               path('<slug:slug>/edit/',
                    login_required(views.CourseEdit.as_view()),
                    name='course_edit'),
               path('<slug:slug>/delete/', views.CourseDelete.as_view(),
                    name='course_delete'),
               path('<slug:slug>/delete-confirm/',
                    views.CourseDeleteConfirm.as_view(),
                    name='course_delete_confirm'),
]
