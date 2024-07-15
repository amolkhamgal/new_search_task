from django.contrib.auth.models import User
from django.db import models

class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.keyword

class SearchResult(models.Model):
    search = models.ForeignKey(Search, related_name='results', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title
