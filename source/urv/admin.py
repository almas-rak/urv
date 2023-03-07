from django.contrib import admin

from urv.models import Employee


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'action_date', 'name', 'stat_urv', 'fact_start', 'being_late', 'end_urv', 'fact_end',
                    'early_departure', 'time_work']

    list_filter = ['id', 'action_date', 'name', 'stat_urv', 'fact_start', 'being_late', 'end_urv', 'fact_end',
                   'early_departure', 'time_work']

    search_fields = ['id', 'action_date', 'name', 'stat_urv', 'fact_start', 'being_late', 'end_urv', 'fact_end',
                     'early_departure', 'time_work']


admin.site.register(Employee, EmployeeAdmin)
