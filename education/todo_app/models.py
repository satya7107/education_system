from django.db import models

# Create your models here.
class todo_details(models.Model):
    task=models.CharField(max_length=50)
    is_complete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.task
        