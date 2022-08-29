from rest_framework import generics, response, status

from reports.models import Trips
import dateutil.parser

from reports.utils import generate_excel_file


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

