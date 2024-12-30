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

    @property
    def class_name_danish(self):
        return "Sted"

    def get_absolute_url(self):
        return reverse("place_list")
    

class Hive(BaseModel):
    number = models.CharField(max_length=8)
    frames = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    place = models.ForeignKey("beejournal.Place", related_name='hives', on_delete=models.PROTECT)

    class Meta:
        unique_together = ['number', 'user', 'place']
        ordering = ['number']
    
    def __str__(self):
        return self.number + " - " + self.place.__str__()

    @property
    def class_name_danish(self):
        return "Stade"

    def frames_or_height(self):
        return self.frames or self.height
    
    def get_absolute_url(self):
        return reverse("hive_list")

    @property
    def queen(self):
        return self.queens.first()

    @property
    def get_inspections(self):
        return self.inspections.all()[:5]


class Queen(BaseModel):
    hive = models.ForeignKey(
        "beejournal.Hive",
        related_name='queens',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    date = models.DateField()
    comment = models.TextField(blank=True, null=True)
    CHOICES = (
        ("white", "Hvid"),
        ("yellow", "Gul"),
        ("red", "Rød"),
        ("green", "Grøn"),
        ("blue", "Blå"),
    )
    color = models.CharField(max_length=8, choices=CHOICES, blank=True, null=True)
    marked = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.hive.__str__() + " - " + str(self.get_color_display())

    @property
    def class_name_danish(self):
        return "Dronning"
    
    def get_absolute_url(self):
        return reverse("queen_list")


class Varroa(BaseModel):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def class_name_danish(self):
        return "Varroa"


class Inspection(BaseModel):
    hive = models.ForeignKey("beejournal.Hive", related_name='inspections', on_delete=models.PROTECT)
    date = models.DateField()
    comment = models.TextField(blank=True, null=True)
    larva = models.BooleanField(default=False)
    egg = models.BooleanField(default=False)
    queen = models.BooleanField(default=False)
    mood = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    varroa = models.ForeignKey(
        "beejournal.Varroa",
        related_name='inspections',
        on_delete=models.PROTECT,
        blank=True, null=True,
    )

    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.hive.__str__() + " - " + self.date.strftime("%Y-%m-%d")

    @property
    def class_name_danish(self):
        return "Inspektion"

    def get_absolute_url(self):
        return reverse("inspection_list")
