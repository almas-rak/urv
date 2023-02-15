from django.db import models


# Create your models here.
class Employee(models.Model):
    action_date = models.DateField(verbose_name='Дата')
    name = models.CharField(max_length=200, null=False, verbose_name='Фамилия Имя')
    stat_urv = models.TimeField(verbose_name='Начало УРВ')
    fact_start = models.TimeField(verbose_name='Фактичесий приход')
    being_late = models.TimeField(verbose_name='Опоздание')
    end_urv = models.TimeField(verbose_name='Конец УРВ')
    fact_end = models.TimeField(verbose_name='Фактический уход')
    early_departure = models.TimeField(verbose_name='Ранний уход')
    time_work = models.TimeField(verbose_name='Отработанное время')
