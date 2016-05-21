from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.company
# Create your models here.
