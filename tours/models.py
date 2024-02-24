from django.db import models


class Person(models.Model):
    name = models.CharField("Name", max_length=200)
    bio = models.TextField("Biography")
    age = models.IntegerField("Age")
    city = models.CharField("Home Town", max_length=200, default="")
    state = models.CharField("State", max_length=200, default="")
    country = models.CharField("Country", max_length=200, default="")
    phone_number = models.CharField("Phone Number", max_length=10, default="")
    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Tourist(Person):
    dates_in_town = models.CharField("Dates in Town", max_length=200, default="")
    activities = models.ManyToManyField("Activity", through="Liked_Activities", related_name="tourists")

    def liked_activities_dict(self):
        return {
            relation.activity.id: {
                'name': relation.activity.name,
                'liked': relation.liked
            }
            for relation in self.liked_activities.filter(liked=True)
        }

class Tour_Guide(Person):
    years_lived = models.IntegerField("Years Lived in City", default=1)
    activities = models.ManyToManyField("Activity", through="Liked_Activities", related_name="tour_guides")
    @property
    def accepted_tourists_dict(self):
        return {
            relation.tourist.id: {
                'name': relation.tourist.name,
                'accepted': relation.accepted
            }
            for relation in self.tourist_relations.filter(accepted=True)
        }

    @property
    def liked_activities_dict(self):
        return {
            relation.activity.id: {
                'name': relation.activity.name,
                'liked': relation.liked
            }
            for relation in self.liked_activities.filter(liked=True)
        }


class Acceptances(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE, related_name='tour_guide_relations')
    tour_guide = models.ForeignKey(Tour_Guide, on_delete=models.CASCADE, related_name='tourist_relations')
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.tourist.name} - {self.tour_guide.name} - {"Accepted" if self.accepted else "Pending"}'

class Activity(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Liked_Activities(models.Model):
    tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE, null=True, blank=True)
    tour_guide = models.ForeignKey(Tour_Guide, on_delete=models.CASCADE, null=True, blank=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    liked = models.BooleanField(default=True)

    class Meta:
        unique_together = (('tourist', 'activity'), ('tour_guide', 'activity'))

    def __str__(self):
        person_name = self.tourist.name if self.tourist else self.tour_guide.name
        return f'{person_name} - {self.activity.name} - {"Liked" if self.liked else "Not Liked"}'