from django.db import models

class Tour_Guide(models.Model):
    name = models.CharField("Name", max_length=200)
    bio = models.TextField("Biography")
    age = models.IntegerField("Age")
    city = models.CharField("Home Town", max_length=200)
    state = models.CharField("State", max_length=200)
    country = models.CharField("Country", max_length=200)
    def __str__(self):
        return self.name


class Tourist(models.Model):
    name = models.CharField("Name", max_length=200)
    age = models.IntegerField()
    bio = models.TextField("Biography")
    city = models.CharField("City", max_length=200)
    state = models.CharField("State", max_length=200)
    likes = models.JSONField(default=list)

    def __str__(self):
        return self.name

