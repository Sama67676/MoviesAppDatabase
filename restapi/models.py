from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=45)
    image = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}-{self.email}'

class Movie(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField('movie_image')
    category = models.CharField(max_length=100, choices=[
        ('Drama', 'Drama'),
        ('Romance', 'Romance'),
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Comedy', 'Comedy'),
        ('Science fiction', 'Science fiction'),
        ('Documentary', 'Documentary'),
        ('Cartoon', 'Cartoon')
    ])

    def __str__(self):
        return f'{self.name}-{self.category}'
