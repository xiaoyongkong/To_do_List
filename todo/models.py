from django.db import models
from django.contrib.auth import get_user_model

class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
      return self.text