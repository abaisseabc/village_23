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
        "check_out_date",
    )


@admin.register(GuestServices)
class GuestServicesAdmin(admin.ModelAdmin):
    list_display = (
        "guest_id_service",
        "get_guests_room_number",
        "get_name_guest",
        "service_name",
    )

    def get_guests_room_number(self, obj):
        return obj.guest_id_service.number_room

    def get_name_guest(self, obj):
        last_name = obj.guest_id_service.last_name
        first_name = obj.guest_id_service.first_name
        middle_name = obj.guest_id_service.middle_name
        return f"{last_name} {first_name} {middle_name}"

    get_guests_room_number.short_description = "Номер комнаты"
    get_name_guest.short_description = "ФИО гостя"
