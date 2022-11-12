from django.db import models


# Create your models here.
class State(models.Model):
    province = models.CharField(max_length=255)

    def __str__(self):
        return self.province


class Data(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    id_province = models.ForeignKey(State, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
