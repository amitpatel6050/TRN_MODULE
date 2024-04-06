
from import_export import resources
from .models import *

class Trn_entryResource(resources.ModelResource):
    class Meta:
        model = Trn_entry

class Unsd_entryResource(resources.ModelResource):
    class Meta:
        model = Unsd_entry

class User_trnResource(resources.ModelResource):
    class Meta:
        model = User_trn

class Sop_masterResource(resources.ModelResource):
    class Meta:
        model = Sop_master

