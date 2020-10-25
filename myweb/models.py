from django.db import models

class Name(models.Model):

    id = models.AutoField(primary_key=True)

    Name = models.IntegerField(default="ชื่อ")

    def __str__(self):
        return f'{self.Name}'

class FoodType(models.Model):
    id = models.AutoField(primary_key=True)
    Food_Type = models.CharField(max_length=100,default="ประเภทอาหาร")

    def __str__(self):
        return f'{self.Food_Type}'

class Food(models.Model):
    Food_Name = models.CharField(max_length=100)
    Price = models.IntegerField()

    FoodType = models.ForeignKey(FoodType, on_delete=models.CASCADE)

    def __str__(self):

        return f'{self.Food_Name} - {self.FoodType} - {self.Name} - {self.Price}'