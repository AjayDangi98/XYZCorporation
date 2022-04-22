from import_export.admin import ImportExportMixin
from django.contrib import admin
from .models import Sales

# Register your models here.
class SalesAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Sales, SalesAdmin)