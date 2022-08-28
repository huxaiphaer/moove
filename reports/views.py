from django.shortcuts import render
from rest_framework import generics, response, status


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
        print("re ", request.data)
        return response.Response({},
                                 status=status.HTTP_400_BAD_REQUEST)

