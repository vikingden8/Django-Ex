from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.title