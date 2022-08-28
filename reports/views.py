from django.shortcuts import render
from rest_framework import generics, response, status

from reports.models import Trips


#
#
# def report_page(request):
#     form = ReportForm()
#
#     print(" form ", form)
#
#     if form.is_valid():
#
#         print(" hi ")
#     return render(request, 'pages/submit_report.html', {"form": form})


class ReportView(generics.ListCreateAPIView):

    """Report View."""

    def create(self, request, *args, **kwargs):
        trips = Trips.objects.filter(
            start='2022-08-14',
            stop='2022-08-22')
        print('trips ', trips)
        return response.Response({},
                                 status=status.HTTP_400_BAD_REQUEST)

