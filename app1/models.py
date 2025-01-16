from django.db import models

# Create your models here.

class App1model(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    address=models.TextField(max_length=200)
    
    def __str__(self):
        return self.name
