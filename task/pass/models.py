from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile (models.Model):
	name=models.CharField(max_length=100)
	#dob=models.DateTimeField()
	passportno=models.CharField(max_length=20,null=True)
	email=models.EmailField(default=True   )
	phoneNumber=models.CharField(max_length=12,default=True)
	img=models.ImageField(upload_to='media/',default='box.jpg',blank=True)

