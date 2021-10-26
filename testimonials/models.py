from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Testimonials(models.Model):
    class Meta:
        verbose_name_plural = "Testimonials"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    comment = models.TextField(max_length=543)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
