from django.contrib import admin
from django.http import HttpResponse
from .models import Car, BookingRequest
import openpyxl
from datetime import datetime

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_day', 'fuel_type', 'transmission', 'seats', 'is_available')
    list_filter = ('fuel_type', 'transmission', 'is_available')
    search_fields = ('name',)
    list_editable = ('is_available',)

@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'car', 'pickup_date', 'return_date', 'status', 'created_at')
    list_filter = ('status', 'pickup_date')
    search_fields = ('customer_name', 'customer_email', 'customer_phone')
    list_editable = ('status',)
    readonly_fields = ('created_at',)
    
    # Add export button
    actions = ['export_to_excel']
    
    def export_to_excel(self, request, queryset):
        # Create Excel file
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Bookings"
        
        # Headers (column names)
        headers = ['ID', 'Customer Name', 'Email', 'Phone', 'Car', 'Pickup Date', 'Return Date', 'Status', 'Message', 'Booking Date']
        ws.append(headers)
        
        # Add data rows
        for booking in queryset:
            ws.append([
                booking.id,
                booking.customer_name,
                booking.customer_email,
                booking.customer_phone,
                booking.car.name,
                booking.pickup_date.strftime('%Y-%m-%d'),
                booking.return_date.strftime('%Y-%m-%d'),
                booking.status,
                booking.message,
                booking.created_at.strftime('%Y-%m-%d %H:%M')
            ])
        
        # Auto-adjust column widths
        for column in ws.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)
            ws.column_dimensions[column_letter].width = adjusted_width
        
        # Create HTTP response
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename=bookings_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
        wb.save(response)
        return response
    
    export_to_excel.short_description = "📊 Export selected bookings to Excel"