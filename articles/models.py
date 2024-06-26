from django.conf import settings
from django.db import models
from django.urls import reverse

class Article(models.Model):
    """News Article"""
    title = models.CharField(max_length = 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_articles",
        blank=True,
    )

    def __str__(self):
        """Article as string"""
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    
    def get_like_url(self):
        """Get like URL based on PK"""
        return reverse("article_like", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    """Comment Model"""

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """Convert to string"""
        return self.body
    
    def get_absolute_url(self):
        return reverse("article_list")
