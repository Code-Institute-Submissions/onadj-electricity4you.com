from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AddNews(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.title + ' | ' + str(self.author)