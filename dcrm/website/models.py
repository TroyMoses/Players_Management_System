from django.db import models


class MalePlayer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	gender =  models.CharField(max_length=20)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	reg_no =  models.CharField(max_length=100)
	course =  models.CharField(max_length=50)
	role = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
		
class FemalePlayer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


	
