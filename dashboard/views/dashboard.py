from rest_framework.views import APIView
from dashboard.models import Orders
from rest_framework.response import Response
from services.models import Services
from django.db.models import Sum, Case, When, DecimalField, Count
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
import calendar


class ClientDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            total_spending = Orders.objects.aggregate(
                total_income=Sum(
                    Case(
                        When(status='completed', client=request.user.profile, then='total_price', ),
                        default=0,
                        output_field=DecimalField()
                    )
                )
            )['total_income']
            order_queryset = Orders.objects.filter(client=request.user.profile)
            total_completed_orders = order_queryset.filter(status='completed', ).count()
            total_cancelled_orders = order_queryset.filter(status='canceled').count()
            total_in_progress_orders = order_queryset.filter(status='in_progress').count()
            return Response({
                'total_spending': total_spending,
                'total_completed_orders': total_completed_orders,
                'total_cancelled_orders': total_cancelled_orders,
                'total_in_progress_orders': total_in_progress_orders

            }, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class ClientMonthSpendingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            current_year = now().year
            month_sales = Orders.objects.filter(
                status='completed',
                client=request.user.profile,
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

            return Response({'month_spending': sorted_month_sales}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class ClientMonthlyNumberOfOrdersView(APIView):

    def get(self, request):
        try:
            current_year = now().year
            month_orders = Orders.objects.filter(
                status='completed',
                client=request.user.profile,
                completed_date__year=current_year
            ).values(
                'completed_date__month'
            ).annotate(
                total_orders=Count('order_number')
            ).order_by('completed_date__month')

            # Initialize a dictionary with all months set to 0
            all_months = {month: 0 for month in range(1, 13)}

            # Update the dictionary with the actual data
            for order in month_orders:
                all_months[order['completed_date__month']] = order['total_orders']

            # Convert the dictionary to a sorted list of dictionaries
            sorted_month_orders = [{'month': calendar.month_name[month], 'total_orders': total_orders} for
                                   month, total_orders in
                                   sorted(all_months.items())]

            return Response({'month_orders': sorted_month_orders}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class SupplierDashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            total_earning = Orders.objects.aggregate(
                total_income=Sum(
                    Case(
                        When(status='completed', service__supplier=request.user.profile, then='total_price', ),
                        default=0,
                        output_field=DecimalField()
                    )
                )
            )['total_income']
            services_queryset = Services.objects.filter(supplier=request.user.profile)
            total_active_services = services_queryset.filter(service_status='Active').count()
            total_inactive_services = services_queryset.filter(service_status='Inactive').count()
            order_queryset = Orders.objects.filter(service__supplier=request.user.profile)
            total_completed_orders = order_queryset.filter(status='completed', ).count()
            total_cancelled_orders = order_queryset.filter(status='canceled').count()
            total_in_progress_orders = order_queryset.filter(status='in_progress').count()
            return Response({
                'total_earning': total_earning,
                'total_completed_orders': total_completed_orders,
                'total_cancelled_orders': total_cancelled_orders,
                'total_in_progress_orders': total_in_progress_orders,
                'total_active_services': total_active_services,
                'total_inactive_services': total_inactive_services

            }, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class SupplierMonthIncomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            current_year = now().year
            month_sales = Orders.objects.filter(
                status='completed',
                service__supplier=request.user.profile,
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

            return Response({'month_income': sorted_month_sales}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class SupplierMonthlyNumberOfOrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            current_year = now().year
            month_orders = Orders.objects.filter(
                status='completed',
                service__supplier=request.user.profile,
                completed_date__year=current_year
            ).values(
                'completed_date__month'
            ).annotate(
                total_orders=Count('order_number')
            ).order_by('completed_date__month')

            # Initialize a dictionary with all months set to 0
            all_months = {month: 0 for month in range(1, 12 + 1)}

            # Update the dictionary with the actual data
            for order in month_orders:
                all_months[order['completed_date__month']] = order['total_orders']

            # Convert the dictionary to a sorted list of dictionaries
            sorted_month_orders = [{'month': calendar.month_name[month], 'total_orders': total_orders} for
                                   month, total_orders in
                                   sorted(all_months.items())]

            return Response({'month_orders': sorted_month_orders}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
