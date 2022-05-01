from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from energy.models import EnergyUsage

@admin.register(EnergyUsage)
class EnergyUsageAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in EnergyUsage._meta.fields]
    search_fields = ['b_name']

