from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class MovieReview(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
    review = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.review



