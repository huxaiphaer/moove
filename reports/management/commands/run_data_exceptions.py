"""Command for Exceptions."""
import requests
from django.core.management.base import BaseCommand

from reports.models import Exceptions, BaseTable, Rule, Diagnostic, Device
from reports.utils import URL, TRIPS_BODY


class Command(BaseCommand):
    help = 'Populate exceptions in the tables'

    def handle(self, *args, **options):

        r = requests.post(url=URL, json=TRIPS_BODY)

        # extracting data in json format
        output = r.json()

        # populate data.
        for result in output['result']:
            data = {
                'distance': result['distance'],
                'active_to': result['activeTo'],
                'active_from': result['activeFrom'],
                'version': result['version'],
                'duration': result['duration'],
                'last_modified_datetime': result['lastModifiedDateTime'],
                'driver': result['driver'],
                'state': result['state'],
                '_id': result['id'],
            }

            if isinstance(result['diagnostic'], dict):
                diagnostic = result['diagnostic']['id']
            else:
                diagnostic = result['diagnostic']
            base_table = BaseTable.objects.create(jsonrpc=output['jsonrpc'])
            exceptions = Exceptions.objects.create(
                **data, base_table_id=base_table)
            Rule.objects.create(
                _id=result['rule']['id'], exceptions_id=exceptions)
            Diagnostic.objects.create(
                _id=diagnostic, exceptions_id=exceptions)
            Device.objects.create(
                geo_tab_id=result['device']['id'], trip_id=None,
                exceptions_id=exceptions)

        print('Exceptions added successfully.')
