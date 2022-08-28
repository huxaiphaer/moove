"""Command for clearing all tables."""
from celery.utils.log import get_task_logger
from django.core.management.base import BaseCommand

from reports.models import (
    BaseTable,
    Trips,
    Driver,
    StopPoint,
    Exceptions,
    Rule,
    Diagnostic,
    Device
)

logger = get_task_logger(__name__)


class Command(BaseCommand):
    help = 'Clear all tables'

    def handle(self, *args, **options):
        BaseTable.objects.all().delete()
        Trips.objects.all().delete()
        Driver.objects.all().delete()
        StopPoint.objects.all().delete()
        Exceptions.objects.all().delete()
        Rule.objects.all().delete()
        Diagnostic.objects.all().delete()
        Device.objects.all().delete()

        print('Operation done.')
