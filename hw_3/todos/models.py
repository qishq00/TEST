from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)  # False - не выполнено, True - выполнено

    def __str__(self):
        return self.title
