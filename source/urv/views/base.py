from datetime import datetime, timedelta, time, date

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from urv.models import Pku
from urv.models import Employee


def index_view(request: WSGIRequest):
    Employees = Employee.objects.filter(action_date=datetime.now())
    return render(request, 'index.html', context={'Employees': Employees})


def get_being_late(stat_urv: time, fact_start: time) -> time:
    if stat_urv > fact_start:
        return time(0)
    being_late = timedelta(hours=fact_start.hour, minutes=fact_start.minute, seconds=fact_start.second) - timedelta(
        hours=stat_urv.hour, minutes=stat_urv.minute, seconds=stat_urv.second)
    a = str(being_late)
    h, m, s = a.split(':')
    being_late = time(hour=int(h), minute=int(m), second=int(s))
    if being_late < time(minute=5):
        return time(0)

    return being_late


def get_early_departure(end_urv: time, fact_end: time) -> time:
    if fact_end > end_urv:
        return time(0)
    early_departure = timedelta(hours=end_urv.hour, minutes=end_urv.minute) - timedelta(hours=fact_end.hour,
                                                                                        minutes=fact_end.minute)
    a = str(early_departure)
    h, m, s = a.split(':')
    early_departure = time(hour=int(h), minute=int(m), second=int(s))
    if early_departure < time(minute=5):
        return time(0)
    return early_departure


def get_time_work(fact_end: time, fact_start: time) -> time:
    if fact_start < time(hour=13) and fact_end > time(hour=14):
        time_work = (timedelta(hours=fact_end.hour,
                               minutes=fact_end.minute) - timedelta(hours=fact_start.hour,
                                                                    minutes=fact_start.minute)) - timedelta(hours=1)

        a = str(time_work)
        h, m, s = a.split(':')
        time_work = time(hour=h, minute=m, second=s)
        return time_work
    elif fact_start > time(hour=13) and fact_end < time(hour=14):
        return time(0)


def test():
    while True:
        db = Pku.objects.using('pku').filter(dev=20, unittype=3)
        for record in db:
            employee = Employee.objects.filter(action_date=record.date, name=record.name)

            if not employee:
                if record.unit == 1:
                    data = {
                        'action_date': record.date,
                        'name': record.name,
                        'stat_urv': time(9),
                        'fact_start': record.time,
                        'being_late': get_being_late(stat_urv=time(9), fact_start=record.time),
                        'end_urv': time(18),
                        'fact_end': time(hour=13),
                        'early_departure': time(0),
                        'time_work': time(0),
                        'db_id': record.pk
                    }
                    a = Employee.objects.create(**data)
                elif record.unit == 2:
                    data = {
                        'action_date': record.date,
                        'name': record.name,
                        'stat_urv': time(9),
                        'fact_start': time(14),
                        'being_late': time(0),
                        'end_urv': time(18),
                        'fact_end': record.time,
                        'early_departure': get_early_departure(fact_end=record.time, end_urv=time(18)),
                        'time_work': time(0),
                        'db_id': record.pk
                    }
                    a = Employee.objects.create(**data)
                else:
                    raise ValueError('ошибка в выборке')
            else:
                employee = employee[0]
                if record.unit == 1:
                    if employee.fact_start > record.time:
                        employee.fact_start = record.time
                        employee.being_late = get_being_late(stat_urv=employee.stat_urv, fact_start=employee.fact_start)
                        employee.time_work = get_time_work(fact_end=employee.fact_end, fact_start=employee.fact_start)
                        employee.save()
                elif record.unit == 2:
                    if employee.fact_end < record.time:
                        employee.fact_end = record.time
                        employee.being_late = get_early_departure(fact_end=record.time, end_urv=employee.end_urv)
                        employee.time_work = get_time_work(fact_end=employee.fact_end, fact_start=employee.fact_start)
                        employee.save()
        break


# a = Employees = Employee.objects.all()
# a.delete()

a = test()
