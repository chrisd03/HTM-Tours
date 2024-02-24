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


class Tourist(Person):
    dates_in_town = models.CharField("Dates in Town", max_length=200, default="")


class Tour_Guide(Person):
    years_lived = models.IntegerField("Years Lived in City", default=1)

    @property
    def accepted_tourists_dict(self):
        return {
            relation.tourist.id: {
                'name': relation.tourist.name,
                'accepted': relation.accepted
            }
            for relation in self.tourist_relations.filter(accepted=True)
        }


class Acceptances(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE, related_name='tour_guide_relations')
    tour_guide = models.ForeignKey(Tour_Guide, on_delete=models.CASCADE, related_name='tourist_relations')
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tourist.name} - {self.tour_guide.name} - {"Accepted" if self.accepted else "Pending"}'
