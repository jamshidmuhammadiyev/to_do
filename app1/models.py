import datetime

from django.db import models

# Create your models here.

class TodoModel(models.Model):
    task=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=datetime.datetime.now)
    updated_at=models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.task

    class Meta:
        db_table='todo'