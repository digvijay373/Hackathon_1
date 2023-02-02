from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class Info(models.Model):
    GPA = models.PositiveIntegerField("GPA", default='', validators=[MinValueValidator(1), MaxValueValidator(5)])
    SATM = models.PositiveIntegerField("SAT MATHS",default='')
    SATE=models.PositiveIntegerField("SAT ENGLISH" ,default='')
    ACT=models.PositiveIntegerField("ACT SCORE" , blank = False)
  