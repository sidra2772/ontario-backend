from rest_framework.views import APIView
from dashboard.models import Orders
from services.models import Services
from userprofile.models import UserProfile
from rest_framework.response import Response
from django.db.models import Sum, Case, When, DecimalField
from rest_framework.permissions import IsAdminUser
from django.utils.timezone import now
import calendar


class DashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        try:
            total_income = Orders.objects.filter(status='completed').aggregate(
                total_income=Sum('total_price')
            )['total_income']

            total_suppliers = UserProfile.objects.filter(user__user_type='supplier').count()
            total_clients = UserProfile.objects.filter(user__user_type='client').count()
            total_active_services = Services.objects.filter(service_status='Active').count()
            total_completed_orders = Orders.objects.filter(status='completed').count()
            total_in_active_services = Services.objects.filter(service_status='Inactive').count()
            total_cancelled_orders = Orders.objects.filter(status='canceled').count()
            total_in_progress_orders = Orders.objects.filter(status='in_progress').count()
            return Response({
                'total_income': total_income,
                'total_suppliers': total_suppliers,
                'total_clients': total_clients,
                'total_active_services': total_active_services,
                'total_completed_orders': total_completed_orders,
                'total_in_active_services': total_in_active_services,
                'total_cancelled_orders': total_cancelled_orders,
                'total_in_progress_orders': total_in_progress_orders

            }, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class MonthlySalesView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        try:
            current_year = now().year
            month_sales = Orders.objects.filter(
                status='completed',
                completed_date__year=current_year
            ).values(
                'completed_date__month'
            ).annotate(
                total_sales=Sum('total_price')
            ).order_by('completed_date__month')

            # Initialize a dictionary with all months set to 0
            all_months = {month: 0 for month in range(1, 13)}

            # Update the dictionary with the actual data
            for sale in month_sales:
                all_months[sale['completed_date__month']] = sale['total_sales']

            # Convert the dictionary to a sorted list of dictionaries
            sorted_month_sales = [{'month': calendar.month_name[month], 'total_sales': total_sales} for
                                  month, total_sales in
                                  sorted(all_months.items())]

            return Response({'month_sales': sorted_month_sales}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
