from rest_framework import generics, response, status

from reports.models import Trips, Vehicle, Exceptions
import dateutil.parser

from reports.serializers import VehicleSerializer, TripsSerializer
from reports.utils import generate_excel_file


class VehicleView(generics.ListAPIView):
    """List all vehicles."""
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class TripView(generics.ListAPIView):
    """List all Trips."""
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer


class ExceptionsView(generics.ListAPIView):
    """List all Exceptions."""
    queryset = Exceptions.objects.all()
    serializer_class = TripsSerializer


class ReportView(generics.ListCreateAPIView):
    """Report View."""

    def create(self, request, *args, **kwargs):

        """ Send a report."""
        try:
            start = dateutil.parser.isoparse(request.data.get('start_date'))
            stop = dateutil.parser.isoparse(request.data.get('end_date'))
            trips = Trips.objects.filter(
                start__gte=start,
                stop__gte=stop)
            generate_excel_file(request.data.get('email'), trips)

            return response.Response({'message': 'Report sent successfully.'},
                                     status=status.HTTP_201_CREATED)
        except Exception as e:
            return response.Response({'message': f'{e}'},
                                     status=status.HTTP_201_CREATED)
