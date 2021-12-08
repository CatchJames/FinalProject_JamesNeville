from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class MovieReview(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(blank=True, null=True)
    review = models.CharField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    title = models.CharField(max_length=200, blank=True, null=True)
    year = models.CharField(max_length=20, blank=True, null=True)
    poster = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.review



