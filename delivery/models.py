from django.db import models
	
class Customer(models.Model):
	Cu_id= models.AutoField(auto_created=True, primary_key=True)
	First_Name = models.CharField(max_length=50)
	Last_Name = models.CharField(max_length=50)
	Email = models.CharField(max_length=50)
	Password  = models.CharField(max_length=50)
	DOB = models.DateField()
	Gender_Choice = (
		('M', 'Male'),('F', 'Female'),('O','Others')
	)
	Gender = models.CharField(max_length=1, choices=Gender_Choice)
	
	class Meta:
		db_table = "Customer_data"
		
		
class Menu(models.Model):
	M_id= models.AutoField(auto_created=True, primary_key=True)
	Food_Name = models.CharField(max_length=50)
	Price = models.IntegerField()
	Image = models.ImageField(default="")
	
	class Meta:
		db_table = "Foodie_menu"
		
