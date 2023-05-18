from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator

SKILL_LEVEL = ((0, "Beginner"), (1, "Intermediate"), (2, "Advanced"))
STATUS = ((0, "Draft"), (1, "Published"))


class Course(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    skill_level = models.IntegerField(choices=SKILL_LEVEL)
    duration_in_hrs = models.DecimalField(max_digits=4, decimal_places=2)
    price_in_gbp = models.DecimalField(max_digits=4, decimal_places=2)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['skill_level']

    def __str__(self):
        return self.title


class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_reviews")
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='reviews')
    written_review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Review {self.written_review} by {self.user}'


class Timetable(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='timetabled_course')
    starts = models.DateTimeField()

    class Meta:
        ordering = ['starts']
        constraints = [
            models.UniqueConstraint(fields=['course', 'starts'],
                                    name='unique_course'),
        ]

    def __str__(self):
        return f'Course {self.course} takes place in the {self.location} on \
            {self.date} from {self.starts} to {self.ends}'


class Booking(models.Model):
    course = models.ForeignKey(Timetable, on_delete=models.CASCADE,
                               related_name='course_bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name="user_bookings")
    places_reserved = models.IntegerField(validators=[MinValueValidator(1), ])
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} has booked onto {self.course}'
