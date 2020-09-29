from django.db import models

# Create your models here.
class user(models.Model):
	first_name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	dob=models.CharField(max_length=11)
	email=models.CharField(max_length=50)
	usrname=models.CharField(max_length=20)
	password=models.CharField(max_length=30)

	def __str__(self):
		return self.usrname

class users(models.Model):
	name=models.CharField(max_length=20)
	dob=models.CharField(max_length=11)
	email=models.CharField(max_length=50)
	usrname=models.CharField(max_length=20)
	password=models.CharField(max_length=30)
	profile_pic=models.FileField(max_length=150)
	contact=models.CharField(max_length=15)
	address=models.CharField(max_length=100)
	status=models.CharField(max_length=10)
	

	def __str__(self):
		return self.usrname

class useractive(models.Model):
	userid=models.CharField(max_length=5) 