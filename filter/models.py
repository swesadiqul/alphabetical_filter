from django.db import models

# Create your models here.
class LetestNews(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=50)
    post_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Letest News"