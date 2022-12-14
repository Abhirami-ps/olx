from django.db import models

# Create your models here.

class Vehicles(models.Model):
    name=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    color=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    transmission=models.CharField(max_length=200)


    def __str__(self):
        return self.name




class Reviews(models.Model):
    vehicle=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    comment=models.CharField(max_length=200)
    rating=models.PositiveIntegerField()
    created_date=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.comment



