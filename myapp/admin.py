from import_export import resources

from django.contrib import admin

from myapp.resources import Trn_entryResource , User_trnResource  , Unsd_entryResource , Sop_masterResource , PunchDataResource ,atteninfoResource ,device_logsResource ,devicelistResource
from .models import User_trn,Trn_entry,Unsd_entry , Sop_master , PunchData ,devicelist , device_logs , atteninfo
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class Trn_entryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Trn_entryResource

class Unsd_entryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Unsd_entryResource


class user_trnAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = User_trnResource

class PunchDataAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PunchDataResource

class Sop_masterAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Sop_masterResource

class atteninfoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = atteninfoResource

class device_logsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = device_logsResource

class devicelistAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = devicelistResource

# class logAdmin(ImportExportModelAdmin, admin.ModelAdmin):
#     resource_class = logResource
  

admin.site.register(User_trn , user_trnAdmin)
admin.site.register(Trn_entry , Trn_entryAdmin)
admin.site.register(Unsd_entry , Unsd_entryAdmin)
admin.site.register(Sop_master , Sop_masterAdmin)
admin.site.register(PunchData , PunchDataAdmin)
admin.site.register(atteninfo , atteninfoAdmin)
admin.site.register(device_logs , device_logsAdmin)
admin.site.register(devicelist , devicelistAdmin)





