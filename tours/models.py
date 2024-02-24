from django.db import models


class Person(models.Model):
    name = models.CharField("Name", max_length=200)
    bio = models.TextField("Biography")
    age = models.IntegerField("Age")
    city = models.CharField("Home Town", max_length=200)
    state = models.CharField("State", max_length=200)
    country = models.CharField("Country", max_length=200)
    phone_number = models.CharField("Phone Number", max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Tour_Guide(Person):
    years_lived = models.IntegerField("Years Lived in City", default=1)


class Tourist(Person):
    likes = models.JSONField(default=list)
    dates_in_town = models.CharField("Dates in Town", max_length=200)

