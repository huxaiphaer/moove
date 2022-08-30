"""File for scheduled tasks."""
from celery.schedules import crontab
from celery.task import periodic_task
from django.core.management import call_command


@periodic_task(
    run_every=(crontab(minute='*/180')),
    name="populate_vehicles",
    ignore_result=True
)
def populate_vehicles():
    """Add data in the Vehicle schema."""
    call_command('clear_all_tables')
    call_command('run_data_exceptions')
    call_command('run_data_vehicles')
