"""File for scheduled tasks."""
from celery import shared_task
from django.core.management import call_command


@shared_task
def populate_data():
    """Add data in all schemas."""
    call_command('clear_all_tables')
    call_command('run_data_exceptions')
    call_command('run_data_vehicles')
    call_command('run_data_trips')
