from django.db import models

# Create your models here.

class Thread(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='posts/', blank=True, null=True)
    description = models.TextField()
    author = models.CharField(max_length=255)
    thread = models.ForeignKey('Thread', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
