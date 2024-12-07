from django.db import models
from django.urls import reverse

from core.models import BaseModel


class Place(BaseModel):
    name = models.CharField(max_length=64)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    @property
    def hive_count(self):
        return self.hives.count()

    def get_absolute_url(self):
        return reverse("place_list")
    


class Hive(BaseModel):
    number = models.CharField(max_length=8)
    frames = models.IntegerField(blank=True, null=True)
    place = models.ForeignKey("beejournal.Place", related_name='hives', on_delete=models.PROTECT)

    class Meta:
        unique_together = ['number', 'user', 'place']
        ordering = ['number']
    
    def __str__(self):
        return self.number + " - " + self.place.__str__()
    
    def get_absolute_url(self):
        return reverse("hive_list")

    @property
    def queen(self):
        return self.queens.first()

    @property
    def get_inspections(self):
        return self.inspections.all()

class Queen(BaseModel):
    hive = models.ForeignKey(
        "beejournal.Hive",
        related_name='queens',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    date = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    CHOICES = (
        ("white", "White"),
        ("yellow", "Yellow"),
        ("red", "Red"),
        ("green", "Green"),
        ("blue", "Blue"),
    )
    color = models.CharField(max_length=8, choices=CHOICES, blank=True, null=True)
    marked = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.hive.__str__() + " - " + str(self.color)
    
    def get_absolute_url(self):
        return reverse("queen_list")


class Inspection(BaseModel):
    hive = models.ForeignKey("beejournal.Hive", related_name='inspections', on_delete=models.PROTECT)
    date = models.DateTimeField()
    comment = models.TextField(blank=True, null=True)
    larva = models.IntegerField(blank=True, null=True)
    egg = models.IntegerField(blank=True, null=True)
    mood = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    varroa = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.hive.__str__() + " - " + self.date.strftime("%Y-%m-%d")

    def get_absolute_url(self):
        return reverse("inspection_list")