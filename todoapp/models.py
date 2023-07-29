from django.db import models

class Todo(models.Model):
    Title=models.CharField(max_length=30)
    Date=models.DateField()
    Priority=models.CharField(max_length=10)