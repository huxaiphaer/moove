"""Command for trips."""
import requests
from django.core.management.base import BaseCommand

from reports.models import Trips, BaseTable, Driver, StopPoint, Device
from reports.utils import URL, EXCEPTIONS_BODY


class Command(BaseCommand):
    help = 'Populate trips in the tables'

    def handle(self, *args, **options):

        r = requests.post(url=URL, json=EXCEPTIONS_BODY)

        # extracting data in json format
        output = r.json()

        # populate data.
        for result in output['result']:
            data = {
                'distance': result['distance'],
                'after_hours_start': result['afterHoursStart'],
                'average_speed': result['averageSpeed'],
                'maximum_speed': result['maximumSpeed'],
                'after_hours_stop_duration': result['afterHoursStopDuration'],
                'speed_range1_duration': result['speedRange1Duration'],
                'work_stop_duration': result['workStopDuration'],
                'driving_duration': result['drivingDuration'],
                '_id': result['id'],
                'idling_duration': result['idlingDuration'],
                'after_hours_distance': result['afterHoursDistance'],
                'start': result['start'],
                'speed_range2': result['speedRange2'],
                'speed_range3': result['speedRange3'],
                'engine_hours': result['engineHours'],
                'speed_range1': result['speedRange1'],
                'stop_duration': result['stopDuration'],
                'is_seat_belt_off': result['isSeatBeltOff'],
                'speed_range2_duration': result['speedRange2Duration'],
                'speed_range3_duration': result['speedRange3Duration'],
                'next_trip_start': result['nextTripStart'],
                'stop': result['stop'],
                'after_hours_driving_duration': result[
                    'afterHoursDrivingDuration'],
                'work_driving_duration': result['workDrivingDuration'],
                'after_hour_send': result['afterHoursEnd'],
                'work_distance': result['workDistance']
            }
            base_table = BaseTable.objects.create(jsonrpc=output['jsonrpc'])
            trip = Trips.objects.create(**data, base_table_id=base_table)
            Driver.objects.create(
                is_driver=result['driver']['isDriver'],
                _id=result['driver']['id'], trip_id=trip)
            StopPoint.objects.create(
                x=result['stopPoint']['x'],
                y=result['stopPoint']['y'],
                trip_id=trip)
            Device.objects.create(
                _id=result['device']['id'], trip_id=trip, exceptions_id=None)

        print('Trips added successfully.')
