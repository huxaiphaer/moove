"""File for scheduled tasks."""
from symbol import test

from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task
def populate_vehicles():
    """Add data in the Vehicle schema."""
    print(' Hi there am good')
    logger.info("The sample task just ran.")
