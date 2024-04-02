from django.contrib import admin

from .models import Guest, GuestServices


# Register your models here.

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = (
        "guest_id",
        "passport",
        "first_name",
        "last_name",
        "middle_name",
        "number_room",
        "check_in_date",
        "check_out_date"
    )


admin.site.register(GuestServices)
