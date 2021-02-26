from django.db import models


class Station(models.Model):
    name = models.CharField("Name", max_length=50, unique=True)
    description = models.TextField("Description")
    image = models.ImageField("Classic Photo", upload_to='stations_photos')
    instagram_url = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Station"
        verbose_name_plural = "Stations"
