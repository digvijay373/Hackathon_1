from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Info(models.Model):
    GPA = models.PositiveIntegerField("GPA", default='', validators=[MinValueValidator(1), MaxValueValidator(5)])
    SATM = models.IntegerField("SAT MATHS",default='')
    SATE=models.IntegerField("SAT ENGLISH" ,default='')
    ACT=models.IntegerField("ACT SCORE" , blank = False)
  