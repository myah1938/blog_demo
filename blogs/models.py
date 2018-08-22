from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    auther = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    