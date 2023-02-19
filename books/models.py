from django.db import models
from people.models import Person
# Create your models here.

class Book(models.Model):
    name = models.CharField(verbose_name='Навазние', max_length=50, blank=True)
    number_pages = models.PositiveBigIntegerField(verbose_name='Количество страниц', blank=True)
    writer = models.ForeignKey(to=Person, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.name}'