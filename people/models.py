from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=50, blank=True)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50, blank=True)
    email = models.EmailField(verbose_name='Эмейл', blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'