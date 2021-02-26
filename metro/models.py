from django.db import models


class Station(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description", blank=True)
    image = models.ImageField("Classic Photo", upload_to='stations_photos', blank=True)
    instagram_url = models.SlugField(max_length=150, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Station"
        verbose_name_plural = "Stations"


class Line(models.Model):
    name = models.CharField("Colour", max_length=50)
    stations = models.ManyToManyField(Station, verbose_name='stations')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Line"
        verbose_name_plural = "Lines"
