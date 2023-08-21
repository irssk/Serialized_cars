from django.db import models


class Auto(models.Model):
    label = models.CharField(max_length=23)
    year = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.label} : {self.price}"

class Owner(models.Model):
    first_name = models.CharField(max_length=23)
    last_name = models.CharField(max_length=23)

    def __str__(self) -> str:
        return f"{self.first_name} : {self.last_name}"


class Auto_Passport(models.Model):
    related_auto = models.OneToOneField(Auto, on_delete=models.CASCADE)
    number = models.IntegerField()
    prefix = models.CharField(max_length=5)

    def __str__(self) -> str:
        return f"{self.related_auto} : {self.prefix, self.number}"

