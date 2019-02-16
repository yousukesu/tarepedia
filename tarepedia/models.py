from django.db import models
from django.utils import timezone


class Post(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    recipe_id = models.IntegerField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    genre = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def private(self):
        self.published_date = None
        self.save()
