
from import_export import resources
from .models import *

class Trn_entryResource(resources.ModelResource):
    class Meta:
        model = Trn_entry


class PunchDataResource(resources.ModelResource):
    class Meta:
        model = PunchData        

class Unsd_entryResource(resources.ModelResource):
    class Meta:
        model = Unsd_entry

class User_trnResource(resources.ModelResource):
    class Meta:
        model = User_trn

class Sop_masterResource(resources.ModelResource):
    class Meta:
        model = Sop_master

class atteninfoResource(resources.ModelResource):
    class Meta:
        model = atteninfo

class device_logsResource(resources.ModelResource):
    class Meta:
        model = device_logs

class devicelistResource(resources.ModelResource):
    class Meta:
        model = devicelist

