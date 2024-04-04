from django.contrib import admin

from .models import CallRequests


# Register your models here.

# admin.site.register(CallRequests)

@admin.register(CallRequests)
class CallRequestsAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "date_added",
    )
