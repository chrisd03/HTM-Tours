from django.db import models


class Person(models.Model):
    name = models.CharField("Name", max_length=200)
    bio = models.TextField("Biography")
    age = models.IntegerField("Age")
    city = models.CharField("Home Town", max_length=200, default="")
    state = models.CharField("State", max_length=200, default="")
    country = models.CharField("Country", max_length=200, default="")
    phone_number = models.CharField("Phone Number", max_length=10, default="")
    likes = models.JSONField(default=list)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Tour_Guide(Person):
    years_lived = models.IntegerField("Years Lived in City", default=1)



class Tourist(Person):
    date_leaving = models.DateField("Date Leaving", max_length=200, default="")


