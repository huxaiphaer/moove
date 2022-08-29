from django.shortcuts import render
from rest_framework import generics, response, status

from reports.models import Trips, Vehicle, Exceptions
import dateutil.parser

from reports.utils import HARSH_ACCELERATION, SPEEDING


class ReportView(generics.ListCreateAPIView):

    """Report View."""

    def create(self, request, *args, **kwargs):
        start = dateutil.parser.isoparse('2022-07-14T22:00:00.000Z')
        stop = dateutil.parser.isoparse('2022-07-22T22:00:00.000Z')
        trips = Trips.objects.filter(
            start__gte=start,
            stop__gte=stop)

        for trip in trips:
            trip_start_date_time = trip.start
            trip_end_date_time = trip.stop
            trip_distance = trip.distance
            vehicle = Vehicle.objects.filter(_id=trip.device._id).first()
            exception_speeding_counts = Exceptions.objects.filter(
                _id=trip.device._id, rule___id=SPEEDING).count()
            exception_harsh_acceleration_counts = Exceptions.objects.filter(
                _id=trip.device._id, rule___id=HARSH_ACCELERATION).count()
            print('---------------------------------------------')
            print('plate number ', vehicle.license_plate)
            print('trip_start_date_time ', trip_start_date_time)
            print('trip_end_date_time ', trip_end_date_time)
            print('trip_distance ', trip_distance)
            print('harsh acceleration ', exception_harsh_acceleration_counts)
            print('speeding ', exception_speeding_counts)
            print('---------------------------------------------')

        return response.Response({},
                                 status=status.HTTP_400_BAD_REQUEST)

