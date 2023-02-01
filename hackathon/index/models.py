from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    mobile_number=models.IntegerField()
    email_address=models.EmailField(default='')
  