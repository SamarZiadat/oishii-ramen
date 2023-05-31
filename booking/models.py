from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

SKILL_LEVEL = ((0, "Beginner"), (1, "Intermediate"), (2, "Advanced"))
STATUS = ((0, "Draft"), (1, "Published"))


class Course(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    skill_level = models.IntegerField(choices=SKILL_LEVEL)
    duration_in_hrs = models.DecimalField(max_digits=4, decimal_places=2)
    price_in_gbp = models.DecimalField(max_digits=5, decimal_places=2)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['skill_level']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns successful post to related slug url"""
        return reverse('course_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


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

    def __str__(self, *args, **kwargs):
        return f'Review {self.written_review} by {self.user}'


class Timetable(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name='timeslots')
    starts = models.DateTimeField()

    class Meta:
        ordering = ['starts']
        constraints = [
            models.UniqueConstraint(fields=['course', 'starts'],
                                    name='unique_course'),
        ]

    def __str__(self):
        return f'Course {self.course} takes place on {self.starts}'


class Booking(models.Model):
    course = models.ForeignKey(Timetable, on_delete=models.CASCADE,
                               related_name='course_bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="user_bookings")
    places_reserved = models.IntegerField(validators=[MinValueValidator(1), ])
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} has booked onto {self.course}'
