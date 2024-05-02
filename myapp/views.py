from django.http import HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from .forms import Trn_entryForm
from django.db.models import Q


from .forms import Unsd_entryForm
from .models import Trn_entry,PunchData
from .models import Unsd_entry
from .models import Sop_master

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
import datetime
from django.http import JsonResponse
import random
from django.conf import settings
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from mysite import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import User_trn, Trn_entry , Sop_master
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# relative import of forms
# Create your views here.


def index(request):
    try:
        user = User_trn.objects.get(email=request.session['email'])

        if user.usertype == "manager" or user.usertype == "verifier" or user.usertype == "approver":
            request.session['email'] = user.email
            request.session['fname'] = user.fname
            request.session['dname'] = user.department

    # request.session['profile_pic']=user.profile_pic.url
            return render(request, 'in.html')
        else:
            request.session['email'] = user.email
            request.session['fname'] = user.fname
            # request.session['profile_pic']=user.profile_pic.url
            return render(request, 'in_operator.html')
    except:
        return render(request, 'index.html')


def validate_email(request):
    email = request.GET.get('email')
    data = {
        'is_taken': User_trn.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)


def login(request):
    if request.method == "POST":
        try:
            user = User_trn.objects.get(email=request.POST['email'])
            user = User_trn.objects.get(
                email=request.POST['email'],
                password=request.POST['password']

            )
            if user.usertype == "manager" or user.usertype == "verifier" or user.usertype == "approver":
                request.session['email'] = user.email
                request.session['fname'] = user.fname
                request.session['dname'] = user.department
            # request.session['profile_pic']=user.profile_pic.url
                return render(request, 'in.html')
            else:
                request.session['email'] = user.email
                request.session['fname'] = user.fname
                # request.session['profile_pic']=user.profile_pic.url
                return render(request, 'in_operator.html')
        except:
            msg = "Email or Password is Incorrect"
            return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, 'login.html')

# def visitor_login(request):
    # if request.method=="POST":
        # try:
        # user=User.objects.get(
        # email=request.POST['email'],
        # password=request.POST['password']

        # )
        # request.session['email']=user.email
        # request.session['fname']=user.fname
        # request.session['profile_pic']=user.profile_pic.url
        # return render(request,'visitor_in.html')
        # except:
        # msg="Email or Password is correct"
        # return render(request,'visitor_in.html',{'msg':msg})
    # else:
        # return render(request,'login.html')


def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        # del request.session['profile_pic']
        return render(request, 'login.html')
    except:
        return render(request, 'login.html')


@csrf_exempt
def trn_signup(request):
     user = User_trn.objects.get(email=request.session['email'])
     if request.method == "POST":
        try:
            Trn_entry.objects.get(cpname=request.POST['cpname'])
            msg="SOP Already Registered"
            return render(request,'Trn_entry.html', {'msg': msg})
        except:

        
         Trn_entry.objects.create(

                trn_created=user,
                cpname=request.POST['cpname'],
                dpname=request.POST['dpname'],
                # sop_name=request.POST['sop_name'],
                # sop_num=request.POST['sop_num'],
               
            )
         msg = "new added"
         return render(request, 'Trn_entry.html', {'msg': msg})
     else:
        msg = ""
        return render(request, 'Trn_entry.html', {'msg': msg})


@csrf_exempt
def unsd_signup(request):
    user = User_trn.objects.get(email=request.session['email'])
    if request.method == "POST":
        # main_series = serial_generate_nrgp(request)
        # descript = request.POST.getlist('desc')
        # quantity = request.POST.getlist('qty')
        # unit = request.POST.getlist('unit')
        # for i in range(0, len(descript)):
        Unsd_entry.objects.create(
                # nrgp_main_serial=i+1,
                # nrgp_serial=main_series,
                unsd_created=user,
                cpname=request.POST['cpname'],
                dpname=request.POST['dpname'],
               
            )

        msg = "Unschedule Traing  Enrollment Successfully"
        return render(request, 'unsd_entry.html', {'msg': msg})
    else:
        msg = ""
        return render(request, 'unsd_entry.html', {'msg': msg})

def back(request):
    user = User_trn.objects.get(email=request.session['email'])
    if user.usertype == "manager" or user.usertype == "verifier" or user.usertype == "approver":
        request.session['email'] = user.email
        request.session['fname'] = user.fname
        # request.session['profile_pic']=user.profile_pic.url
        return render(request, 'in.html')
    else:
        request.session['email'] = user.email
        request.session['fname'] = user.fname
        # request.session['profile_pic']=user.profile_pic.url
        return render(request, 'in_operator.html')
        # except:
        # msg="Email or Password is Incorrect"
        # return render(request,'in.html',{'msg':msg})

    # else:
        # return render(request,'visitor_in.html')
    # return render(request,'in.html')


def change_password(request):
    if request.method == "POST":
        user = User_trn.objects.get(email=request.session['email'])
        if user.password == request.POST['old_password']:
            if request.POST['new_password'] == request.POST['cnew_password']:
                user.password = request.POST['new_password']
                user.save()
                return redirect('logout')
            else:
                msg = "New password & Confirm New Password Does Not matched"
                return render(request, 'change_password.html', {'msg': msg})
        else:
            msg = "Old Password does Not Matched"
            return render(request, 'change_password.html', {'msg': msg})

    else:
        return render(request, 'change_password.html')


def new_password(request):
    email = request.POST['email']
    np = request.POST['new_password']
    cnp = request.POST['cnew_password']

    if np == cnp:
        user = User_trn.objects.get(email=email)
        user.password = np
        user.save()
        msg = "Password Updated Successfully"
        return render(request, 'login.html', {'msg': msg})
    else:
        msg = "New Password & Confirm New Password Does Not Matched"
        return render(request, 'new_password.html', {'email': email, 'msg': msg})

from itertools import zip_longest

def trn_view(request):
    trn_entrys = Trn_entry.objects.filter(
        trn_created__department=request.session['dname'], current_status="Entry").order_by("-id")
    # id_list=trn_entrys.emp_name.split(",")
    # user_data=User_trn.objects.filter(id__in=id_list)
    # print("User_data",user_data)
    # print(trn_entrys)
    user_data_list = []
    punch_data_list = []
    for trn_entry in trn_entrys:
        if  trn_entry.emp_name != None:
            email_list = trn_entry.emp_name.split(",")
            user_data = User_trn.objects.filter(email__in=email_list)
            user_data_list.append(user_data)

            punch_data = PunchData.objects.filter(Q(email__in=email_list) & Q(out_date__isnull=False)).order_by("-out_date")
            punch_data_list.append(punch_data)
        else:
            # user_data_list.append([])
            user_data_list.append(User_trn.objects.none())
            punch_data_list.append(PunchData.objects.none())
    # print("cjkdhjkcd",user_data_list)
    all_data=zip_longest(trn_entrys, user_data_list)
    # print(dict(all_data))
    return render(request, 'trn_view.html', {'trn_entrys': trn_entrys,"all_data":all_data})





def unsd_exit(request, pk):
    all_in_user = Unsd_entry.objects.filter(current_status="Entry")
    if request.method == "GET":
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        unsd_entrys.current_status = "Exit"
        unsd_entrys.unsd_exit_time = datetime.datetime.now()
        unsd_entrys.save()
        msg = "Exit Successfully"
        return render(request, 'unsd_view.html', {'msg': msg, 'unsd_entrys': all_in_user})
    else:
        return render(request, 'unsd_view.html', {'unsd_entrys': all_in_user})


def trn_print(request, pk):
    user_detail = Trn_entry.objects.get(id=pk)
    return render(request, 'trn_print.html', {'user_detail': user_detail})


def unsd_view(request):
    # if request.method=="POST":
    unsd_entrys = Unsd_entry.objects.filter(
        unsd_created__department=request.session['dname'], current_status="Entry").order_by("-id")
    return render(request, 'unsd_view.html', {'unsd_entrys': unsd_entrys})


def log_print(request, pk):
    user_detail = Trn_entry.objects.get(id=pk)
    return render(request, 'log_print.html', {'user_det': user_detail})


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Trn_entry, Unsd_entry, id=id)

    # pass the object as instance in form
    form = Trn_entryForm, Unsd_entry(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


def send_email(request, pk):
    if request.method == "POST":
        trn_entrys = Trn_entry.objects.get(id=pk)
        subject = 'Material Receipt Details'
        message = f"Concern Person Name :- {trn_entrys.cpname}\n Department Name :- {trn_entrys.dpname}\n Service Provide Name:-{trn_entrys.spname}\n Description :- {trn_entrys.desc}\n Unit :- {trn_entrys.unit}\n Quantity  :- {trn_entrys.qty}\n Remarks  :- {trn_entrys.remarks}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]
        send_mail(subject, message, email_from, recipient_list)
        msg = "E-Mail Sent Successfully"
        return render(request, 'send_email.html', {'trn_entrys': trn_entrys, 'msg': msg})
    else:
        trn_entrys = Trn_entry.objects.get(id=pk)
        return render(request, 'send_email.html', {'trn_entrys': trn_entrys})


def unsd_send_email(request, pk):
    if request.method == "POST":
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        subject = 'RGP Details'
        message = f"Concern Person Name :- {unsd_entrys.cpname}\n Department Name :- {unsd_entrys.dpname}\n Service Provide Name:-{unsd_entrys.spname}\n Description :- {unsd_entrys.desc}\n Unit :- {unsd_entrys.unit}\n Quantity  :- {unsd_entrys.qty}\n Remarks  :- {unsd_entrys.remarks}"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]
        send_mail(subject, message, email_from, recipient_list)
        msg = "E-Mail Sent Successfully"
        return render(request, 'unsd_send_email.html', {'unsd_entrys': unsd_entrys, 'msg': msg})
    else:
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        return render(request, 'unsd_send_email.html', {'unsd_entrys': unsd_entrys})

def verify_link(request,ver, pk, status):
    rgp_data = Trn_entry.objects.get(id=pk)
    verifier_per=User_trn.objects.get(id=ver)
    rgp_data.verify_status = bool(status)
    if status == 1:
        rgp_data.rgp_verify_time = timezone.now()
        rgp_data.verifier=verifier_per
        rgp_data.save()
    elif status==0:
        rgp_data.rgp_verify_time = None
        rgp_data.verifier = None
        rgp_data.save()
    return render(request, "verified.html")

# def verify_link(request, pk, status):
#     rgp_data = Trn_entry.objects.get(id=pk)
#     rgp_data.verify_status = bool(status)
#     rgp_data.rgp_verify_time = timezone.now()
#     rgp_data.save()
#     return render(request, "verified.html")

def unsd_verify_link(request, ver, pk, status):
    rgp_data = Unsd_entry.objects.get(id=pk)
    verifier_per = User_trn.objects.get(id=ver)
    rgp_data.unsd_verify_status = bool(status)
    if status == 1:
        rgp_data.unsd_verify_time = timezone.now()
        rgp_data.unsd_verifier = verifier_per
        rgp_data.save()
    elif status == 0:
        rgp_data.unsd_verify_time = None
        rgp_data.unsd_verifier = None
        rgp_data.save()
    return render(request, "verified.html")

def unsd_verify_link_all(request, ver, pk, status):
    all_data = Unsd_entry.objects.filter(nrgp_serial=pk)
    verifier_per = User_trn.objects.get(id=ver)
    for rgp_data in all_data:
        rgp_data.nrgp_verify_status = bool(status)
        if status == 1:
            rgp_data.nrgp_verify_time = timezone.now()
            rgp_data.nrgp_verifier = verifier_per
            rgp_data.save()
        elif status == 0:
            rgp_data.nrgp_verify_time = None
            rgp_data.nrgp_verifier = None
            rgp_data.save()
    return render(request, "verified.html")

# def nrgp_verify_link(request, pk, status):
#     rgp_data = Unsd_entry.objects.get(id=pk)
#     rgp_data.nrgp_verify_status = bool(status)
#     rgp_data.nrgp_verify_time = timezone.now()
#     rgp_data.save()
#     return render(request, "verified.html")

# <a href=f"{request.get_host()}/verify_link/{pk}/1"><button>Verify<button></a>

def send_email_verify(request, pk):
    user_data = User_trn.objects.filter(
        usertype="verifier", department=request.session['dname'])
    # user_data = User_trn.objects.all()
    if request.method == "POST":

        trn_entrys = Trn_entry.objects.get(id=pk)
        subject = 'SCHEDULE TRAINING VERIFICATION'
        # verify_link = quote(f"{request.get_host()}/verify_link/{pk}/1")
        # unverify_link = quote(f"{request.get_host()}/verify_link/{pk}/0")

        # message = f"""
        # Concern Person Name :- {trn_entrys.cpname}\n Department Name :- {trn_entrys.dpname}\n Service Provide Name:-{trn_entrys.spname}\n Description :- {trn_entrys.desc}\n Unit :- {trn_entrys.unit}\n Quantity  :- {trn_entrys.qty}\n Remarks  :- {trn_entrys.remarks}
        # verify----"{request.get_host()}/verify_link/{pk}/1"

        # Not Verify----"{request.get_host()}/verify_link/{pk}/0"

        # verify={verify_link}

        # not verify={unverify_link}

        # """
        # send_mail(subject, message, email_from, recipient_list)
        sel = User_trn.objects.get(email=request.POST['email'])
        ver=sel.id
        verify = f"{request.get_host()}/verify_link/{ver}/{pk}/1"
        notverify = f"{request.get_host()}/verify_link/{ver}/{pk}/0"
        content = {
            "verify": verify,
            "notverify": notverify,
            "pname": trn_entrys.cpname,
            "dname": trn_entrys.dpname,
            "sop_ver": trn_entrys.sop_ver,
            "trnr_name": trn_entrys.trnr_name,
            "trnr_dept": trn_entrys.trnr_dept,
            "trnr_desn": trn_entrys.trnr_desn,
            "vanue": trn_entrys.vanue,
            # "type_trn": trn_entrys.type_trn,
            "mode_trn": trn_entrys.mode_trn, 
            "emp_name_assign": trn_entrys.emp_name_assign,
            "va": "VERIFY",
            "va1": "NOT VERIFY"
        }

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]
        html_content = render_to_string(
            "rgp_verify.html", content)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            subject, text_content, email_from, recipient_list)
        email.attach_alternative(html_content, "text/html")
        email.send()

        msg = "E-Mail Sent Successfully"
        # verifier_email = User_trn.objects.get(email=request.POST['email'])
        # trn_entrys.verifier = verifier_email
        # trn_entrys.save()
        return render(request, 'send_email_verify.html', {'trn_entrys': trn_entrys, 'msg': msg, 'user_data': user_data})
    else:
        trn_entrys = Trn_entry.objects.get(id=pk)
        return render(request, 'send_email_verify.html', {'trn_entrys': trn_entrys, 'user_data': user_data})



def unsd_send_email_verify(request, pk):
    user_data = User_trn.objects.filter(
        usertype="verifier", department=request.session['dname'])
    # user_data = User_trn.objects.all()
    if request.method == "POST":

        unsd_entrys = Unsd_entry.objects.get(id=pk)
        subject = 'UNSCHEDULE TRAINING VERIFY'
   
        sel = User_trn.objects.get(email=request.POST['email'])
        ver=sel.id
        verify = f"{request.get_host()}/unsd_verify_link/{ver}/{pk}/1"
        notverify = f"{request.get_host()}/unsd_verify_link/{ver}/{pk}/0"
        content = {
            "verify": verify,
            "notverify": notverify,
            "pname": unsd_entrys.cpname,
            "dname": unsd_entrys.dpname,
            "sop_ver": unsd_entrys.sop_ver,
            "trnr_name": unsd_entrys.trnr_name,
            "trnr_dept": unsd_entrys.trnr_dept,
            "trnr_desn": unsd_entrys.trnr_desn,
            "vanue": unsd_entrys.vanue,
            # "type_trn": unsd_entrys.type_trn,
            "mode_trn": unsd_entrys.mode_trn,
            "emp_name": unsd_entrys.emp_name,
            "va": "VERIFY",
            "va1": "NOT VERIFY"
        }

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]
        html_content = render_to_string(
            "nrgp_verify.html", content)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            subject, text_content, email_from, recipient_list)
        email.attach_alternative(html_content, "text/html")
        email.send()

        msg = "E-Mail Sent Successfully"
        # verifier_email = User_trn.objects.get(email=request.POST['email'])
        # trn_entrys.verifier = verifier_email
        # trn_entrys.save()
        return render(request, 'unsd_send_email_verify.html', {'unsd_entrys': unsd_entrys, 'msg': msg, 'user_data': user_data})
    else:
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        return render(request, 'unsd_send_email_verify.html', {'unsd_entrys': unsd_entrys, 'user_data': user_data})



# def unsd_send_email_verify(request, pk,):
#     user_data = User_trn.objects.filter(
#         usertype="verifier", department=request.session['dname'])
#     if request.method == "POST":
#         unsd_entrys = Unsd_entry.objects.get(id=pk)
#         # id_data = Unsd_entry.objects.filter(nrgp_serial=vid)
#         subject = 'TRAINING VERIFICATION'
#         sel = User_trn.objects.get(email=request.POST['email'])
#         ver = sel.id
#         content = {}
#         for i in id_data:
#             verify = f"{request.get_host()}/nrgp_verify_link/{ver}/{i.id}/1"
#             notverify = f"{request.get_host()}/nrgp_verify_link/{ver}/{i.id}/0"
#             # verify_all = f"{request.get_host()}/nrgp_verify_link_all/{ver}/{vid}/1"
#             content.update({i.id: {"id": i.id,
#                                    "verify": verify,
#                                    "notverify": notverify,
#                                 #    "verify_all": verify_all,
#                                    "pname": unsd_entrys.cpname,
#                                     "dname": unsd_entrys.dpname,
#                                     "sop_ver": unsd_entrys.sop_ver,
#                                     "trnr_name": unsd_entrys.trnr_name,
#                                     "trnr_dept": unsd_entrys.trnr_dept,
#                                     "trnr_desn": unsd_entrys.trnr_desn,
#                                     "vanue": unsd_entrys.vanue,
#                                     "type_trn": unsd_entrys.type_trn,
#                                     "mode_trn": unsd_entrys.mode_trn,
#                                    "va": "VERIFY",
#                                    "va1": "NOT VERIFY"}
#                             })
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [request.POST['email']]
#         html_content = render_to_string(
#             "nrgp_verify.html", {"content": content})
#         text_content = strip_tags(html_content)
#         email = EmailMultiAlternatives(
#             subject, text_content, email_from, recipient_list)
#         email.attach_alternative(html_content, "text/html")
#         email.send()
#         msg = "E-Mail Sent Successfully"
#         return render(request, 'unsd_send_email_verify.html', {'unsd_entrys': unsd_entrys, 'msg': msg, 'user_data': user_data, "id_data": id_data})
#     else:
#         unsd_entrys = Unsd_entry.objects.get(id=pk)
#         return render(request, 'unsd_send_email_verify.html', {'unsd_entrys': unsd_entrys, 'user_data': user_data})
    


 
def approve_link(request,apr, pk, status):
    trn_data = Trn_entry.objects.get(id=pk)
    apr_per = User_trn.objects.get(id=apr)
    trn_data.approve_status = bool(status)
    if status == 1:
        trn_data.trn_approve_time = timezone.now()
        trn_data.approver = apr_per
        trn_data.save()
    elif status == 0:
        trn_data.trn_approve_time = None
        trn_data.approver = None
        trn_data.save()
    return render(request, "approved.html")


def unsd_approve_link(request,apr, pk, status):
    rgp_data = Unsd_entry.objects.get(id=pk)
    apr_per = User_trn.objects.get(id=apr)
    rgp_data.unsd_approve_status = bool(status)
    if status == 1:
        rgp_data.unsd_approve_time = timezone.now()
        rgp_data.unsd_approver = apr_per
        rgp_data.save()
    elif status == 0:
        rgp_data.unsd_approve_time = None
        rgp_data.unsd_approver = None
        rgp_data.save()
    return render(request, "approved.html")

def unsd_approve_link_all(request, apr, pk, status):
    all_data = Unsd_entry.objects.filter(nrgp_serial=pk)
    apr_per = User_trn.objects.get(id=apr)
    for rgp_data in all_data:
        rgp_data.nrgp_approve_status = bool(status)
        if status == 1:
            rgp_data.nrgp_approve_time = timezone.now()
            rgp_data.nrgp_approver = apr_per
            rgp_data.save()
        elif status == 0:
            rgp_data.nrgp_approve_time = None
            rgp_data.nrgp_approver = None
            rgp_data.save()
    return render(request, "approved.html")


def send_email_approve(request, pk):
    user_data = User_trn.objects.filter(
        usertype="approver")
    if request.method == "POST":
        trn_entrys = Trn_entry.objects.get(id=pk)
        subject = 'SCHEDULE TRAINING APPROVE'
        sel = User_trn.objects.get(email=request.POST['email'])
        apr = sel.id
        verify = f"{request.get_host()}/approve_link/{apr}/{pk}/1"
        notverify = f"{request.get_host()}/approve_link/{apr}/{pk}/0"
        content = {
            "verify": verify,
            "notverify": notverify,
            "pname": trn_entrys.dpname,
            "dname": trn_entrys.cpname,
            "sop_ver": trn_entrys.sop_ver,
            "trnr_name": trn_entrys.trnr_name,
            "trnr_dept": trn_entrys.trnr_dept,
            "trnr_desn": trn_entrys.trnr_desn,
            "vanue": trn_entrys.vanue,
            # "type_trn": trn_entrys.type_trn,
            "mode_trn": trn_entrys.mode_trn,
            "emp_name_assign": trn_entrys.emp_name_assign,
            "va": "APPROVE",
            "va1": "NOT APPROVE"
        }

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]
        html_content = render_to_string(
            "sop_approve.html", content)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            subject, text_content, email_from, recipient_list)
        email.attach_alternative(html_content, "text/html")
        email.send()
        msg = "E-Mail Sent Successfully"
        return render(request, 'send_email_approve.html', {'trn_entrys': trn_entrys, 'msg': msg, 'user_data': user_data})
    else:
        trn_entrys = Trn_entry.objects.get(id=pk)
        return render(request, 'send_email_approve.html', {'trn_entrys': trn_entrys, 'user_data': user_data})
    

def unsd_send_email_approve(request, pk):
    user_data = User_trn.objects.filter(
        usertype="approver")
    if request.method == "POST":
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        subject = 'UNSCHEDULE TRAINING APPROVE'
        sel = User_trn.objects.get(email=request.POST['email'])
        apr = sel.id
        verify = f"{request.get_host()}/unsd_approve_link/{apr}/{pk}/1"
        notverify = f"{request.get_host()}/unsd_approve_link/{apr}/{pk}/0"
        content = {
            "verify": verify,
            "notverify": notverify,
            "pname": unsd_entrys.cpname,
            "dname": unsd_entrys.dpname,
            "sop_ver": unsd_entrys.sop_ver,
            "trnr_name": unsd_entrys.trnr_name,
            "trnr_dept": unsd_entrys.trnr_dept,
            "trnr_desn": unsd_entrys.trnr_desn,
            "vanue": unsd_entrys.vanue,
            # "type_trn": unsd_entrys.type_trn,
            "mode_trn": unsd_entrys.mode_trn,
            "emp_name": unsd_entrys.emp_name,
            "va": "APPROVE",
            "va1": "NOT APPROVE"
        }

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email']]
        html_content = render_to_string(
            "unsd_sop_approve.html", content)
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            subject, text_content, email_from, recipient_list)
        email.attach_alternative(html_content, "text/html")
        email.send()
        msg = "E-Mail Sent Successfully"
        return render(request, 'unsd_send_email_approve.html', {'unsd_entrys': unsd_entrys, 'msg': msg, 'user_data': user_data})
    else:
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        return render(request, 'unsd_send_email_approve.html', {'unsd_entrys': unsd_entrys, 'user_data': user_data})





# def unsd_send_email_approve(request, pk, vid):
#     # user_data = User_trn.objects.get(usertype="approver")
#     # user_data = User_trn.objects.all()
#     user_data = User_trn.objects.filter(
#         usertype="approver")
#     if request.method == "POST":
#         unsd_entrys = Unsd_entry.objects.get(id=pk)
#         id_data = Unsd_entry.objects.filter(nrgp_serial=vid)
#         subject = 'NRGP APPROVE'
#         sel = User_trn.objects.get(email=request.POST['email'])
#         apr = sel.id
#         content = {}
#         for i in id_data:
#             verify = f"{request.get_host()}/unsd_approve_link/{apr}/{i.id}/1"
#             notverify = f"{request.get_host()}/unsd_approve_link/{apr}/{i.id}/0"
#             verify_all = f"{request.get_host()}/unsd_approve_link_all/{apr}/{vid}/1"
#             content.update({i.id: {
#                 "id": i.id,
#                 "verify": verify,
#                 "notverify": notverify,
#                 "verify_all": verify_all,
#                 "pname": i.cpname,
#                 "dname": i.dpname,
#                 "sname": i.spname,
#                 "desc": i.desc,
#                 "unit": i.unit,
#                 "qty": i.qty,
#                 "remarks": i.remarks,
#                 "va": "APPROVE",
#                 "va1": "NOT APPROVE"
#             }})
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [request.POST['email']]
#         html_content = render_to_string(
#             "nrgp_approve.html", {"content": content})
#         text_content = strip_tags(html_content)
#         email = EmailMultiAlternatives(
#             subject, text_content, email_from, recipient_list)
#         email.attach_alternative(html_content, "text/html")
#         email.send()
#         msg = "E-Mail Sent Successfully"
#         # approver_email = User_trn.objects.get(email=request.POST['email'])
#         # unsd_entrys.nrgp_approver = approver_email
#         # unsd_entrys.save()
#         return render(request, 'unsd_send_email_approve.html', {'unsd_entrys': unsd_entrys, 'msg': msg, 'user_data': user_data})
#     else:
#         unsd_entrys = Unsd_entry.objects.get(id=pk)
#         return render(request, 'unsd_send_email_approve.html', {'unsd_entrys': unsd_entrys, 'user_data': user_data})


# def rgp_search(request):
#     if request.method == "POST":
#         # try:
#         # user_detail = Trn_entry.objects.get(id=pk)
#         # signups=Signup.objects.all()
#         return render(request, 'register_rgp.html')
#         # except:
#         # msg = "Invalid RGP Number"
#         # return render(request, 'rgp_search.html', {'msg': msg})
#     else:
#         return render(request, 'rgp_search.html')


def trn_all(request):
    log_data = Trn_entry.objects.filter(
        trn_created__department=request.session['dname'])  # .order_by('-id')[:3]
    return render(request, 'trn_all.html', {'log_data': log_data})


def unsd_all(request):
    log_data = Unsd_entry.objects.filter(
        unsd_created__department=request.session['dname'])  # .order_by('-id')[:3]
    return render(request, 'unsd_all.html', {'log_data': log_data})


# def unsd_print(request, pk):
#     user_detail = Unsd_entry.objects.filter(nrgp_serial=pk)
#     single_data = Unsd_entry.objects.filter(nrgp_serial=pk).last()

#     return render(request, 'unsd_print.html', {'user_detail': user_detail, "single_data": single_data})


def unsd_print(request, pk):
    user_detail = Unsd_entry.objects.get(id=pk)
    return render(request, 'unsd_print.html', {'user_detail': user_detail})

# def rgp_outward(request, pk):
#     if request.method == "POST":
#         trn_entrys = Trn_entry.objects.get(id=pk)
#         user = User_trn.objects.get(email=request.session['email'])
#         trn_entrys.outward_sender = user
#         trn_entrys.outward_status = True
#         trn_entrys.outward_mode = request.POST['tmode']
#         trn_entrys.outward_reciever_name = request.POST['rname']
#         trn_entrys.rgp_outward_time = timezone.now()
#         trn_entrys.save()
#         msg = "RGP product Outward successfully"
#         return render(request, 'rgp_outward.html', {'trn_entrys': trn_entrys, 'msg': msg})
#     else:
#         trn_entrys = Trn_entry.objects.get(id=pk)
#         return render(request, 'rgp_outward.html', {'trn_entrys': trn_entrys})


# def nrgp_outward(request, pk):
#     if request.method == "POST":
#         unsd_entrys = Unsd_entry.objects.get(id=pk)
#         user = User_trn.objects.get(email=request.session['email'])
#         unsd_entrys.nrgp_outward_sender = user
#         unsd_entrys.nrgp_outward_status = True
#         unsd_entrys.nrgp_outward_mode = request.POST['tmode']
#         unsd_entrys.nrgp_outward_reciever_name = request.POST['rname']
#         unsd_entrys.current_status="Exit"
#         unsd_entrys.nrgp_outward_time = timezone.now()
#         unsd_entrys.save()
#         msg = "NRGP product Outward successfully"
#         return render(request, 'nrgp_outward.html', {'unsd_entrys': unsd_entrys, 'msg': msg})
#     else:
#         unsd_entrys = Unsd_entry.objects.get(id=pk)
#         return render(request, 'nrgp_outward.html', {'unsd_entrys': unsd_entrys})


# def rgp_inward(request, pk):
#     if request.method == "POST":
#         trn_entrys = Trn_entry.objects.get(id=pk)
#         user = User_trn.objects.get(email=request.session['email'])
#         trn_entrys.inward_receiver = user
#         trn_entrys.inward_status = True
#         trn_entrys.outward_status = True
#         trn_entrys.inward_party_challan = request.POST['pcnumber']
#         trn_entrys.inward_mode = request.POST['vnumber']
#         trn_entrys.rgp_inward_time = timezone.now()
#         trn_entrys.save()
#         msg = "RGP product Inward successfully"
#         return render(request, 'rgp_inward.html', {'trn_entrys': trn_entrys, 'msg': msg})
#     else:
#         trn_entrys = Trn_entry.objects.get(id=pk)
#         return render(request, 'rgp_inward.html', {'trn_entrys': trn_entrys})


# def nrgp_view_operator(request):
#     unsd_entrys = Unsd_entry.objects.filter(
#         current_status="Entry", nrgp_approve_status=True)
#     return render(request, 'nrgp_view_operator.html', {'unsd_entrys': unsd_entrys})


def serial_generate(request):
    now = datetime.datetime.now()
    try:
        latest = Trn_entry.objects.last()
        var3 = latest.rgp_serial
        var4 = int(var3[:-5])+1
        return str(var4)+"-"+str(now.year)
    except:
        var3 = "1"+"-"+str(now.year)
        return var3
    
def main_series_generate(request):
    now = datetime.datetime.now()
    try:
        latest = Unsd_entry.objects.last()
        var3 = latest.nrgp_main_serial
        var4 = int(var3)+1
        return str(var4)
    except:
        var3 = "1"
        return var3

def serial_generate_nrgp(request):
    now = datetime.datetime.now()
    try:
        latest = Unsd_entry.objects.last()
        var3 = latest.nrgp_serial
        var4 = int(var3[:-5])+1
        return str(var4)+"-"+str(now.year)
    except:
        var3 = "1"+"-"+str(now.year)
        return var3


def trn_edit(request, pk):
    if request.method == "POST":
        trn_entrys = Trn_entry.objects.get(id=pk)
        user = User_trn.objects.get(email=request.session['email'])
        trn_entrys.rgp_edit = user
        MY_EMP=request.POST.getlist('emp_name_assign[]')
        trn_entrys.sop_ver = request.POST['sver']
        trn_entrys.trnr_name = request.POST['trn_nm']
        trn_entrys.trnr_dept = request.POST['trn_dp']
        trn_entrys.trnr_desn = request.POST['trn_dgn']
        trn_entrys.emp_name_assign = ','.join(MY_EMP)
        trn_entrys.vanue = request.POST['vnu']
        trn_entrys.reason = request.POST['reason']
        # trn_entrys.type_trn = request.POST['type_trn']
        trn_entrys.mode_trn = request.POST['mode_trn']
        trn_entrys.trn_edit_status = True      
        trn_entrys.trn_edit_time = timezone.now()
        trn_entrys.save()
        msg = "Training updated successfully"
        return render(request, 'trn_edit.html', {'trn_entrys': trn_entrys, 'msg': msg})
    else:
        
        trn_entrys = Trn_entry.objects.get(id=pk)
        email_list=trn_entrys.emp_name_assign.split(",")
        user_data=User_trn.objects.filter(email__in=email_list)
        return render(request, 'trn_edit.html', {'trn_entrys': trn_entrys , 'user_data':user_data})
    

def unsd_edit(request, pk):
    if request.method == "POST":
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        user = User_trn.objects.get(email=request.session['email'])
        unsd_entrys.rgp_edit = user
        MY_EMP=request.POST.getlist('emp_name[]')
        unsd_entrys.sop_ver = request.POST['sver']
        unsd_entrys.trnr_name = request.POST['trn_nm']
        unsd_entrys.trnr_dept = request.POST['trn_dp']
        unsd_entrys.trnr_desn = request.POST['trn_dgn']
        unsd_entrys.emp_name = ','.join(MY_EMP)
        unsd_entrys.vanue = request.POST['vnu']
        unsd_entrys.reason = request.POST['reason']
        # unsd_entrys.type_trn = request.POST['type_trn']
        unsd_entrys.mode_trn = request.POST['mode_trn']      
        unsd_entrys.trn_edit_time = timezone.now()
        unsd_entrys.unsd_edit_status = True 
        unsd_entrys.save()
        msg = "Training updated successfully"
        return render(request, 'unsd_edit.html', {'unsd_entrys': unsd_entrys, 'msg': msg})
    else:
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        email_list=unsd_entrys.emp_name.split(",")
        user_data=User_trn.objects.filter(email__in=email_list)
        return render(request, 'unsd_edit.html', {'unsd_entrys': unsd_entrys, 'user_data':user_data})
    


# def trn_assign(request):
#     # if request.method=="POST":
#     trn_entrys = Trn_entry.objects.filter(
#         rgp_created__department=request.session['dname'], current_status="Entry")
#     return render(request, 'trn_view.html', {'trn_entrys': trn_entrys})


def trn_assign(request, pk):
   trn_entrys = Trn_entry.objects.get(id=pk)
   user = User_trn.objects.get(email=request.session['email'])
#    trn_entrys.rgp_edit = user
   user_data = User_trn.objects.filter(
       
        usertype="operator", department=request.session['dname'])
    # user_data = User_trn.objects.all()
   if request.method == "POST":
        # print( request.POST.getlist('emp_name[]'))
        trn_entrys = Trn_entry.objects.get(id=pk)
        MY_EMP=request.POST.getlist('emp_name[]')
        # sel = User_trn.objects.get(email=request.POST['email'])
        trn_entrys.emp_name =','.join(MY_EMP)
        trn_entrys.sch_date = request.POST['sch_date']
        trn_entrys.trn_asgn_status = True
        trn_entrys.sop_assign_time = timezone.now()
        trn_entrys.save()

        msg = "SOP Assign Successfully"
        
        return render(request, 'Assign_SOP.html', {'trn_entrys': trn_entrys, 'msg': msg, 'user_data': user_data})
   else:
        trn_entrys = Trn_entry.objects.get(id=pk)
        return render(request, 'Assign_SOP.html', {'trn_entrys': trn_entrys, 'user_data': user_data})
   


# def un_trn_assign(request, pk):
#    user_data = User_trn.objects.filter(
#         usertype="operator", department=request.session['dname'])
#     # user_data = User_trn.objects.all()
#    if request.method == "POST":

#         unsd_entrys = Unsd_entry.objects.get(id=pk)
       
#         sel = User_trn.objects.get(email=request.POST['email'])
        

#         msg = "SOP Assign Successfully"
        
#         return render(request, 'unschedule_trn.html', {'unsd_entrys': unsd_entrys, 'msg': msg, 'user_data': user_data})
#    else:
#         unsd_entrys = Unsd_entry.objects.get(id=pk)
#         return render(request, 'unschedule_trn.html', {'unsd_entrys': unsd_entrys, 'user_data': user_data})


def un_trn_assign(request, pk):
    user_data = User_trn.objects.filter(
        usertype="operator", department=request.session['dname'])
    if request.method == "POST":
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        # id_data = Unsd_entry.objects.filter(nrgp_serial=vid)
        # subject = 'NRGP VERIFY'
        sel = User_trn.objects.get(email=request.POST['email'])
        # ver = sel.id
        # content = {}
        # for i in id_data:
        #     verify = f"{request.get_host()}/nrgp_verify_link/{ver}/{i.id}/1"
        #     notverify = f"{request.get_host()}/nrgp_verify_link/{ver}/{i.id}/0"
        #     verify_all = f"{request.get_host()}/nrgp_verify_link_all/{ver}/{vid}/1"
        #     content.update({i.id: {"id": i.id,
        #                            "verify": verify,
        #                            "notverify": notverify,
        #                            "verify_all": verify_all,
        #                            "pname": i.cpname,
        #                            "dname": i.dpname,
        #                            "sname": i.spname,
        #                            "desc": i.desc,
        #                            "unit": i.unit,
        #                            "qty": i.qty,
        #                            "remarks": i.remarks,
        #                            "va": "VERIFY",
        #                            "va1": "NOT VERIFY"}
        #                     })
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [request.POST['email']]
        # html_content = render_to_string(
        #     "nrgp_verify.html", {"content": content})
        # text_content = strip_tags(html_content)
        # email = EmailMultiAlternatives(
        #     subject, text_content, email_from, recipient_list)
        # email.attach_alternative(html_content, "text/html")
        # email.send()
        msg = "Training Assigned Successfully"
        return render(request, 'unschedule_trn.html', {'unsd_entrys': unsd_entrys, 'msg': msg, 'user_data': user_data})
    else:
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        return render(request, 'unschedule_trn.html', {'unsd_entrys': unsd_entrys, 'user_data': user_data})
    



# def trn_view(request, pk):
#    user_data = User_trn.objects.filter(
#         usertype="operator", department=request.session['dname'])
#     # user_data = User_trn.objects.all()
#    if request.method == "POST":

#         trn_entrys = Trn_entry.objects.get(id=pk)
       
#         sel = User_trn.objects.get(email=request.POST['email'])
        

#         msg = "SOP Assign Successfully"
        
#         return render(request, 'trn_view.html', {'trn_entrys': trn_entrys, 'msg': msg, 'user_data': user_data})
#    else:
#         trn_entrys = Trn_entry.objects.get(id=pk)
#         return render(request, 'trn_view.html', {'trn_entrys': trn_entrys, 'user_data': user_data})
   


def trn_attend(request , pk):
    if request.method == "POST":
        trn_entrys = Trn_entry.objects.get(id=pk)
        user = User_trn.objects.get(email=request.session['email'])
        trn_entrys.trn_sender = user
        trn_entrys.sop_ver = request.POST['sver']
        MY_EMP=request.POST.getlist('emp_name[]')
        trn_entrys.trnr_name = request.POST['trn_nm']
        trn_entrys.trnr_dept = request.POST['trn_dp']
        trn_entrys.trnr_desn = request.POST['trn_dgn']
        trn_entrys.vanue = request.POST['vnu']
        # trn_entrys.type_trn = request.POST['type_trn']
        trn_entrys.mode_trn = request.POST['mode_trn']
        trn_entrys.emp_name_assign = ','.join(MY_EMP)
        trn_entrys.trn_attend_status = True
        trn_entrys.trn_attend_time = timezone.now()
        trn_entrys.save()
        msg = "Training updated successfully"
        return render(request, 'trn_view01.html', {'trn_entrys': trn_entrys, 'msg': msg})
    else:
        trn_entrys = Trn_entry.objects.get(id=pk)
        email_list=trn_entrys.emp_name.split(",")
        user_data=User_trn.objects.filter(email__in=email_list)
        return render(request, 'trn_view01.html', {'trn_entrys': trn_entrys,'user_data':user_data})
    
    

def untrn_view(request , pk):
   
    unsd_entrys = Unsd_entry.objects.get(id=pk)
    user = User_trn.objects.get(email=request.session['email'])
        # user_data = User_trn.objects.all()
    # user_data = User_trn.objects.filter(
       
    #     usertype="operator", department=request.session['dname'])
    user_data = User_trn.objects.all()

    if request.method == "POST":
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        unsd_entrys.trn_sender = user
        unsd_entrys.sop_ver = request.POST['sver']
        MY_EMP=request.POST.getlist('emp_name[]')
        unsd_entrys.emp_name =','.join(MY_EMP)
        unsd_entrys.trnr_name = request.POST['trn_nm']
        unsd_entrys.trnr_dept = request.POST['trn_dp']
        unsd_entrys.trnr_desn = request.POST['trn_dgn']
        unsd_entrys.vanue = request.POST['vnu']
        # unsd_entrys.type_trn = request.POST['type_trn']
        unsd_entrys.mode_trn = request.POST['mode_trn']
        unsd_entrys.unsd_asgn_status = True
        unsd_entrys.unsd_assign_time = timezone.now()
        # unsd_entrys.trn_attend_time = timezone.now()
        unsd_entrys.save()
        msg = "Training updated successfully"
        return render(request, 'untrn_view.html', {'unsd_entrys': unsd_entrys, 'msg': msg, 'user_data': user_data})
    else:
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        # email_list=unsd_entrys.emp_name.split(",")
        # user_data=User_trn.objects.filter(email__in=email_list)
        return render(request, 'untrn_view.html', {'unsd_entrys': unsd_entrys, 'user_data': user_data})
    


def back_assign(request):
        
    user = User_trn.objects.get(email=request.session['email'])
    trn_entrys = Trn_entry.objects.filter(trn_created__department=request.session['dname'], current_status="Entry")
    if user.usertype == "manager" or user.usertype == "verifier" or user.usertype == "approver":
    
        request.session['email'] = user.email
        request.session['fname'] = user.fname
       
        return render(request, 'trn_view.html' , {'trn_entrys': trn_entrys})
    else:
        request.session['email'] = user.email
        request.session['fname'] = user.fname
       
        return render(request, 'trn_view.html' , {'trn_entrys': trn_entrys})
    

def back_assign_unsd(request):
        
    user = User_trn.objects.get(email=request.session['email'])
    unsd_entrys = Unsd_entry.objects.filter(unsd_created__department=request.session['dname'], current_status="Entry")
    if user.usertype == "manager" or user.usertype == "verifier" or user.usertype == "approver":
    
        request.session['email'] = user.email
        request.session['fname'] = user.fname
       
        return render(request, 'unsd_view.html' , {'unsd_entrys': unsd_entrys})
    else:
        request.session['email'] = user.email
        request.session['fname'] = user.fname
       
        return render(request, 'unsd_view.html' , {'unsd_entrys': unsd_entrys})
    


def trn_start(request, pk):
    if request.method == "POST":
        trn_entrys = Trn_entry.objects.get(id=pk)
        user = User_trn.objects.get(email=request.session['email'])
        trn_entrys.rgp_edit = user
        trn_entrys.trn_start_status = True
        trn_entrys.trn_start_time = timezone.now()
        trn_entrys.save()
        msg = "Training Started successfully"
        return render(request, 'trn_start.html', {'trn_entrys': trn_entrys, 'msg': msg})
    else:
        trn_entrys = Trn_entry.objects.get(id=pk)
        return render(request, 'trn_start.html', {'trn_entrys': trn_entrys})
    
def trn_end(request, pk):
    if request.method == "POST":
        trn_entrys = Trn_entry.objects.get(id=pk)
        user = User_trn.objects.get(email=request.session['email'])
        trn_entrys.rgp_edit = user
        trn_entrys.trn_end_status = True
        trn_entrys.trn_end_time = timezone.now()
        trn_entrys.save()
        msg = "Training End successfully"
        return render(request, 'trn_end.html', {'trn_entrys': trn_entrys, 'msg': msg})
    else:
        trn_entrys = Trn_entry.objects.get(id=pk)
        return render(request, 'trn_end.html', {'trn_entrys': trn_entrys})
    

def trn_evaluation(request , pk):
    if request.method == "POST":
        trn_entrys = Trn_entry.objects.get(id=pk)
        user = User_trn.objects.get(email=request.session['email'])
        trn_entrys.rgp_edit = user
        trn_entrys.viva_voice = request.POST['eva_voice']
        trn_entrys.trn_evalu_status = True
        trn_entrys.trn_evalu_time = timezone.now()

        # trn_entrys.written_test = request.POST['written_test']
        trn_entrys.save()
        msg = "Training Evaluation successfully"
        return render(request, 'trn_evaluation.html', {'trn_entrys': trn_entrys, 'msg': msg})
    else:
        trn_entrys = Trn_entry.objects.get(id=pk)
        return render(request, 'trn_evaluation.html', {'trn_entrys': trn_entrys})
   
   

def trn_written(request):
   
    return render(request, 'trn_written.html')


def unsd_start(request, pk):
    if request.method == "POST":
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        user = User_trn.objects.get(email=request.session['email'])
        unsd_entrys.rgp_edit = user
        unsd_entrys.trn_start_time = timezone.now()
        unsd_entrys.unsd_start_status = True
        unsd_entrys.save()
        msg = "Training Started successfully"
        return render(request, 'unsd_start.html', {'unsd_entrys': unsd_entrys, 'msg': msg})
    else:
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        return render(request, 'unsd_start.html', {'unsd_entrys': unsd_entrys})
    
           
def unsd_end(request, pk):
   if request.method == "POST":
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        user = User_trn.objects.get(email=request.session['email'])
        unsd_entrys.rgp_edit = user
        unsd_entrys.trn_end_time = timezone.now()
        unsd_entrys.unsd_end_status = True
        unsd_entrys.save()
        msg = "Training End successfully"
        return render(request, 'unsd_end.html', {'unsd_entrys': unsd_entrys, 'msg': msg})
   else:
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        return render(request, 'unsd_end.html', {'unsd_entrys': unsd_entrys})
   
    
def unsd_evaluation(request , pk):
    if request.method == "POST":
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        user = User_trn.objects.get(email=request.session['email'])
        unsd_entrys.rgp_edit = user
        unsd_entrys.viva_voice = request.POST['eva_voice']
        unsd_entrys.unsd_evalu_status = True
        unsd_entrys.unsd_evalu_time = timezone.now()
        # trn_entrys.written_test = request.POST['written_test']
        unsd_entrys.save()
        msg = "Training Evaluation successfully"
        return render(request, 'unsd_evaluation.html', {'unsd_entrys': unsd_entrys, 'msg': msg})
    else:
        unsd_entrys = Unsd_entry.objects.get(id=pk)
        return render(request, 'unsd_evaluation.html', {'unsd_entrys': unsd_entrys})

def unsd_written(request):
   
    return render(request, 'unsd_written.html')

def trn_exit(request, pk):
    all_in_user = Trn_entry.objects.filter(
        current_status="Entry", trn_created__department=request.session['dname'])
    if request.method == "GET":
        trn_entrys = Trn_entry.objects.get(id=pk)
        trn_entrys.trn_exit_time = datetime.datetime.now()
        trn_entrys.current_status = "Exit"
        trn_entrys.save()
        return redirect("trn_view")
        # msg = "Exit Successfully"
        # return render(request, 'trn_view.html', {'msg': msg, 'trn_entrys': all_in_user})
    else:
        return render(request, 'trn_view.html', {'trn_entrys': all_in_user})
    
def view_matrix(request, pk):
    user_detail = Trn_entry.objects.get(id=pk)
    return render(request, 'view_matrix.html', {'user_detail': user_detail})


@csrf_exempt
def sop_in(request):
     user = User_trn.objects.get(email=request.session['email'])
     if request.method == "POST":
        try:
            Sop_master.objects.get(sop_no=request.POST['sop_no'])
            msg="SOP Already Registered"
            return render(request,'sop_entry.html', {'msg': msg})
        except:

        
         Sop_master.objects.create(

                trn_created=user,
                sop_name=request.POST['sop_name'],
                sop_no=request.POST['sop_no'],
                # sop_name=request.POST['sop_name'],
                # sop_num=request.POST['sop_num'],
               
            )
         msg = "new added"
         return render(request, 'sop_entry_new.html', {'msg': msg})
     else:
        msg = ""
        return render(request, 'sop_entry_new.html', {'msg': msg})
     
def sop_search(request):
	if request.method=="POST":
		try:
			trn_entrys=Trn_entry.objects.get(cpname=request.POST['cpname'])
			#signups=Signup.objects.all()
			return render(request,'sop_re_entry.html',{'trn_entrys':trn_entrys})
		except:
			msg="SOP Number not register"
			return render(request,'sop_entry_new.html',{'msg':msg})
	else:
		return render(request,'sop_entry_new.html')
    

def sop_create(request , pk):
    if request.method == "POST":
        trn_entrys = Trn_entry.objects.get(id=pk)
        user = User_trn.objects.get(email=request.session['email'])
        trn_entrys.trn_sender = user
        
       
        
        # trn_entrys.current_status = Entry
        trn_entrys.sop_create_time = timezone.now()
        trn_entrys.save()
        msg = "Training created successfully"
        return render(request, 'sop_re_entry.html', {'trn_entrys': trn_entrys, 'msg': msg})
    else:
        
        return render(request, 'sop_re_entry.html', {'trn_entrys': trn_entrys})