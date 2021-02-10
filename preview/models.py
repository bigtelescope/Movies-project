from django.db import models


class Category(models.Model):
    name = models.CharField("Category", max_length=100)
    text = models.TextField("Description")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to='pictures/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Human"
        verbose_name_plural = "Humans"


class Genre(models.Model):
    name = models.CharField("Genre", max_length=100)
    text = models.TextField("Description")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Movie(models.Model):
    title = models.CharField("Genre", max_length=100)
    tagline = models.CharField("Genre", max_length=100)
    description = models.TextField("Description")
    poster = models.ImageField("Image", upload_to='pictures/')
    year = models.PositiveSmallIntegerField("Premiere date", default=0)
    actors = models.ManyToManyField
