from django.db import models


# Create your models here.
class client(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
class Meta:
        db_table = "client"
        
class appointment(models.Model):
    patient=models.CharField(max_length=50)
    doctor=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    phn=models.IntegerField()
    smpt=models.CharField(max_length=100)
class Meta:
        db_table = "appointment" 
        
        
class bloodbank(models.Model):
    name=models.CharField(max_length=50)
    # bloodtype=models.CharField(max_length=50)
    phone=models.IntegerField()
class Meta:
        db_table = "bloodbank"