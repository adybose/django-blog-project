from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    # def __str__(self):
    #     return self.title