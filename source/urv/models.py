from django.db import models


# Create your models here.
class Employee(models.Model):
    action_date = models.DateField(verbose_name='Дата')
    name = models.CharField(max_length=200, verbose_name='Фамилия Имя')
    stat_urv = models.TimeField(verbose_name='Начало УРВ')
    fact_start = models.TimeField(default=0, verbose_name='Фактичесий приход')
    being_late = models.TimeField(default=0, verbose_name='Опоздание')
    end_urv = models.TimeField(verbose_name='Конец УРВ')
    fact_end = models.TimeField(verbose_name='Фактический уход')
    early_departure = models.TimeField(default=0, verbose_name='Ранний уход')
    time_work = models.TimeField(default=0, verbose_name='Отработанное время')
    db_id = models.IntegerField(verbose_name='id с другой БД')


class Pku(models.Model):
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    event = models.SmallIntegerField(blank=True, null=True)
    dev = models.SmallIntegerField(blank=True, null=True)
    unit = models.SmallIntegerField(blank=True, null=True)
    unittype = models.SmallIntegerField(blank=True, null=True)
    part = models.SmallIntegerField(blank=True, null=True)
    accessarea = models.SmallIntegerField(blank=True, null=True)
    descr = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pku'

    # def __str__(self):
    #     return f'{self.date} {self.time}, {self.name}'
