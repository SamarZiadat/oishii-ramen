from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator

SKILL_LEVEL = ((0, "Beginner"), (1, "Intermediate"), (2, "Advanced"))
LOCATION = ((0, "Kitchen, Oishii Ramen"), (1, "Workshop Room, Oishii Ramen"))


class Course(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    skill_level = models.IntegerField(choices=SKILL_LEVEL)
    location = models.IntegerField(choices=LOCATION)
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['skill_level']

    def __str__(self):
        return self.title


class Review(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='reviews')
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_reviews")
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review {self.message} by {self.username}'


class Timetable(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='timetabled_course')
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    location = models.CharField(max_length=200)

    class Meta:
        ordering = ['starts']
        constraints = [
            models.UniqueConstraint(fields=['course', 'starts'],
                                    name='unique_course'),
        ]

    def __str__(self):
        return f'Course {self.course} takes place from {self.starts} \
            to {self.ends}'


class Booking(models.Model):
    course = models.ForeignKey(Timetable, on_delete=models.CASCADE,
                               related_name='course_bookings')
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_bookings")
    places_reserved = models.IntegerField(validators=[MinValueValidator(1), ])
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username} has booked onto {self.course}'
