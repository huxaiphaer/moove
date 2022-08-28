"""File for scheduled tasks."""
from symbol import test

from celery import shared_task
from celery.utils.log import get_task_logger

from reports.models import Vehicle

logger = get_task_logger(__name__)


@shared_task
def populate_vehicles():
    """Add data in the Vehicle schema."""
    Vehicle.objects.create()
