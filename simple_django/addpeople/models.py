from django.db import models

# Create your models here.


class People(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    age = models.IntegerField()
    sex = models.CharField(max_length=6)
    createdBy = models.IntegerField(null=True)

    def __str__(self):
        return self.firstName + "  " + self.lastName + " " + str(self.age) + " " + self.sex + "\n"        