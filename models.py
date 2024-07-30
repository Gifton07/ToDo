from django.db import models

# Create your models here.
class store(models.Model):
    task_name=models.CharField(max_length=250)
    priority =models.IntegerField()
    status =models.BooleanField(default=False)
    date=models.DateField()



    def __str__(self):
        return self.task_name

