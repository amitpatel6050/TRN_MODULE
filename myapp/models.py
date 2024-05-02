from django.db import models
from random import choices
from secrets import choice
from turtle import position
from django.db import models
from django.utils import timezone


user_type = (
    ("operator", "operator"),
    ("manager", "manager"),
    ("approver", "approver"),
    ("verifier", "verifier"),
    ("disable", "disable")
)
dept = (
    ("admin", "admin"),
    ("HR", "HR"),
    ("QA", "QA"),
    ("QC", "QC"),
    ("PH", "PH"),
    ("WH", "WH"),
    ("ENGG", "ENGG"),
    ("API", "API"),
    ("ADL", "ADL"),
    ("EOHS", "EOHS"),
    ("IT", "IT"),
    ("NONE", "NONE")
)

# Create your models here.


class User_trn(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100, choices=user_type)
    department=models.CharField(max_length=100,choices=dept,null=True)
    def __str__(self):
        return self.fname+" "+self.lname+" "+self.department+" "+self.usertype
    
class Sop_master(models.Model):
    sop_name = models.CharField(max_length=100)
    sop_no = models.CharField(max_length=100)
    current_status = models.CharField(max_length=10, default="Entry")
    trn_created = models.ForeignKey(
        User_trn, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.sop_name+" "+self.sop_no


from django.db import models

class PunchData(models.Model):
    email = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=45, null=True, default=None)
    in_time = models.DateTimeField(null=True, default=None)
    out_date = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'punch_data'

from django.db import models

class atteninfo(models.Model):
    AttenID = models.CharField(max_length=20)
    empcode = models.CharField(max_length=20)
    intime = models.DateField()
    outtime = models.DateField()
    

  
    def __str__(self):
        return self.AttenID
    

from django.db import models

class device_logs(models.Model):
    devicelogsid = models.CharField(max_length=20)
    empcode = models.CharField(max_length=20)
    logdatetime = models.DateField()
    direction_type = models.CharField(max_length=20)
    trn_flag = models.CharField(max_length=20)
    
    

   
    def __str__(self):
        return self.devicelogsid


from django.db import models

class devicelist(models.Model):
    # ID_device = models.CharField(max_length=20)
    Device_name = models.CharField(max_length=20)
    IPAddress = models.CharField(max_length=20)
    Logs = models.CharField(max_length=20)
    direction_type = models.CharField(max_length=20)
    # class Meta:
    #     # Define custom table name if needed
    #     db_table = 'device_logs'

        # Define custom primary key field
        # Here we explicitly set the primary key to 'id' and 
        # tell Django not to automatically add its own primary key field
        # This is done to avoid conflicts
        # primary_key = models.AutoField(primary_key=True, db_column='id')
    

    def __str__(self):
        return self.Device_name






class Trn_entry(models.Model):
    # rgp_serial = models.CharField(max_length=20, null=True)
    trn_created = models.ForeignKey(
        User_trn, on_delete=models.CASCADE, null=True)
    current_status = models.CharField(max_length=10, default="Entry")
    cpname = models.CharField(max_length=100)
    sop_create_time = models.DateTimeField( null=True)
    dpname = models.CharField(max_length=100)
    emp_name = models.CharField(max_length=100, null=True)
    emp_name_assign = models.CharField(max_length=100, null=True)
    sch_date = models.CharField(max_length=100, null=True)
    trn_asgn_status = models.BooleanField(default=False)
    sop_assign_time = models.DateTimeField( null=True)
   
    sop_ver = models.CharField(max_length=100, null=True)
    trnr_name = models.CharField(max_length=100, null=True)
    trnr_dept = models.CharField(max_length=100, null=True)
    trnr_desn = models.CharField(max_length=100, null=True)
    vanue = models.CharField(max_length=100, null=True)
    # type_trn = models.CharField(max_length=100, null=True)
    mode_trn = models.CharField(max_length=100, null=True)
    trn_attend_status = models.BooleanField(default=False)
    trn_attend_time = models.DateTimeField( null=True)
   
    reason = models.CharField(max_length=100, null=True)
    trn_edit_status = models.BooleanField(default=False)
    trn_edit_time = models.DateTimeField( null=True)
    
    trn_start_time = models.DateTimeField( null=True)
    trn_start_status = models.BooleanField(default=False)
   
    trn_end_time = models.DateTimeField( null=True)
    trn_end_status = models.BooleanField(default=False)
    
    viva_voice = models.CharField(max_length=100, null=True)
    written_test = models.CharField(max_length=100, null=True)
    trn_evalu_status = models.BooleanField(default=False)
    trn_evalu_time = models.DateTimeField( null=True)
   
    trn_one_status = models.BooleanField(default=False)
    trn_exit_time = models.DateTimeField( null=True)
    operator = models.ForeignKey(
        User_trn, related_name='operator', null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(
        User_trn, related_name='manager', null=True, on_delete=models.CASCADE)
    trn_approve_time = models.DateTimeField( null=True)
    







    # spname = models.CharField(max_length=100)
    # desc = models.CharField(max_length=100)
    # unit = models.CharField(max_length=100)
    # qty = models.CharField(max_length=100)
    # remarks = models.CharField(max_length=100)
    # date = models.DateTimeField(default=timezone.now)
    # made_on = models.DateTimeField(default=timezone.now)
    # current_status = models.CharField(max_length=10, default="Entry")
    verifier = models.ForeignKey(
        User_trn, related_name='verifier', null=True, on_delete=models.CASCADE)
    verify_status = models.BooleanField(default=False)
    rgp_verify_time = models.DateTimeField(null=True)
    approver = models.ForeignKey(
        User_trn, related_name='approver', null=True, on_delete=models.CASCADE)
    approve_status = models.BooleanField(default=False)
    # rgp_approve_time = models.DateTimeField( null=True)

    # outward_sender = models.ForeignKey(
    #     User_trn, related_name='outward_sender', on_delete=models.CASCADE, null=True)
    # outward_status = models.BooleanField(default=False)
    # outward_mode = models.CharField(max_length=100, null=True)
    # outward_reciever_name = models.CharField(max_length=100, null=True)
    # rgp_outward_time = models.DateTimeField( null=True)

    # inward_receiver = models.ForeignKey(
    #     User_trn, related_name='inward_receiver', on_delete=models.CASCADE, null=True)
    # inward_status = models.BooleanField(default=False)
    # inward_party_challan = models.CharField(max_length=100, null=True)
    # inward_mode = models.CharField(max_length=100, null=True)
    # rgp_inward_time = models.DateTimeField(null=True)


    # rgp_edit = models.ForeignKey(
    #     User_trn, related_name='rgp_edit', on_delete=models.CASCADE, null=True)
    # # inward_status = models.BooleanField(default=False)
    # reason_edit = models.CharField(max_length=100, null=True)
    # # inward_mode = models.CharField(max_length=100, null=True)
    # rgp_edit_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.dpname


class Unsd_entry(models.Model):
    # nrgp_main_serial=models.CharField(null=True,default=0,max_length=20)
    # nrgp_serial = models.CharField(max_length=20, null=True)

    current_status = models.CharField(max_length=10, default="Entry")
    cpname = models.CharField(max_length=100)
    dpname = models.CharField(max_length=100)
    # sop_name = models.CharField(max_length=100)
    # sop_num = models.CharField(max_length=100)
    sop_ver = models.CharField(max_length=100, null=True)
    trnr_name = models.CharField(max_length=100, null=True)
    trnr_dept = models.CharField(max_length=100, null=True)
    trnr_desn = models.CharField(max_length=100, null=True)
    vanue = models.CharField(max_length=100, null=True)
    type_trn = models.CharField(max_length=100, null=True)
    mode_trn = models.CharField(max_length=100, null=True)
    trn_attend_time = models.DateTimeField( null=True)
    reason = models.CharField(max_length=100, null=True)
    trn_edit_time = models.DateTimeField( null=True)
    trn_start_time = models.DateTimeField( null=True)
    trn_end_time = models.DateTimeField( null=True)
    viva_voice = models.CharField(max_length=100, null=True)
    written_test = models.CharField(max_length=100, null=True)
    unsd_asgn_status = models.BooleanField(default=False)
    unsd_assign_time = models.DateTimeField( null=True)
    unsd_attend_status = models.BooleanField(default=False)
    # unsd_attend_time = models.DateTimeField( null=True)
    unsd_edit_status = models.BooleanField(default=False)
    # unsd_edit_time = models.DateTimeField( null=True)
    # unsd_start_time = models.DateTimeField( null=True)
    unsd_start_status = models.BooleanField(default=False)
    # unsd_end_time = models.DateTimeField( null=True)
    unsd_end_status = models.BooleanField(default=False)
    unsd_evalu_status = models.BooleanField(default=False)
    unsd_evalu_time = models.DateTimeField( null=True)
    unsd_exit_time = models.DateTimeField( null=True)
    emp_name = models.CharField(max_length=100, null=True)






    unsd_created = models.ForeignKey(
        User_trn, on_delete=models.CASCADE, null=True)
    # cpname = models.CharField(max_length=100)
    # dpname = models.CharField(max_length=100)
    # spname = models.CharField(max_length=100)
    # desc = models.CharField(max_length=100)
    # unit = models.CharField(max_length=100)
    # qty = models.CharField(max_length=100)
    # remarks = models.CharField(max_length=100)
    # date = models.DateTimeField(default=timezone.now)
    # made_on = models.DateTimeField(default=timezone.now)
    # current_status = models.CharField(max_length=10, default="Entry")
    unsd_verifier = models.ForeignKey(
        User_trn, related_name='nrgp_verifier', null=True, on_delete=models.CASCADE)
    unsd_verify_status = models.BooleanField(default=False)
    unsd_verify_time = models.DateTimeField( null=True)
    unsd_approver = models.ForeignKey(
        User_trn, related_name='nrgp_approver', null=True, on_delete=models.CASCADE)
    unsd_approve_status = models.BooleanField(default=False)
    unsd_approve_time = models.DateTimeField(null=True)
    # nrgp_outward_sender = models.ForeignKey(
    #     User_trn, related_name='nrgp_outward_sender', on_delete=models.CASCADE, null=True)
    # nrgp_outward_status = models.BooleanField(default=False)
    # nrgp_outward_mode = models.CharField(max_length=100, null=True)
    # nrgp_outward_reciever_name = models.CharField(max_length=100, null=True)
    # nrgp_outward_time = models.DateTimeField( null=True)


    # nrgp_edit = models.ForeignKey(
    #     User_trn, related_name='nrgp_edit', on_delete=models.CASCADE, null=True)
    # # inward_status = models.BooleanField(default=False)
    # reason_edit = models.CharField(max_length=100, null=True)
    # # inward_mode = models.CharField(max_length=100, null=True)
    # nrgp_edit_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.dpname

# class rgp_outward(models.Model):
#     rgp_product = models.ForeignKey(
#         Rgp_entry, on_delete=models.CASCADE, null=True)
#     mode=models.CharField(max_length=100,null=True)
#     reciever_name=models.CharField(max_length=100,null=True)
