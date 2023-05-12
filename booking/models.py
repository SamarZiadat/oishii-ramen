from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    skill_level = models.IntegerField(choices=SKILLLEVEL)
    location = models.CharField(max_length=100, unique=True)
    duration_hrs = models.DecimalField(max_digits=1, decimal_places=2)
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