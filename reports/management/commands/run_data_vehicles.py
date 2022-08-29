"""Command for vehicles."""
import requests
from django.core.management.base import BaseCommand

from reports.models import Trips, BaseTable, Driver, StopPoint, Device, Vehicle
from reports.utils import URL, VEHICLE_BODY


class Command(BaseCommand):
    help = 'Populate vehicles in the tables'

    def handle(self, *args, **options):

        r = requests.post(url=URL, json=VEHICLE_BODY)

        # extracting data in json format
        output = r.json()

        # populate data.
        for result in output['result']:
            data = {
                "_id": result["id"],
                "license_plate": result["licensePlate"]
            }
            base_table = BaseTable.objects.create(jsonrpc=output['jsonrpc'])
            Vehicle.objects.create(**data, base_table_id=base_table)

        print('Vehicles added successfully.')
