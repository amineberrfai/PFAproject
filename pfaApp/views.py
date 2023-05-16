from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from .models import *
import csv


def ViewPage(request):
    return render(request, "home.html")


def UserReg(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        receId = request.POST['receId']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # User already exist or not

        user = RegiUser.objects.filter(Email=email)

        if user:
            message = "User Already Exists"
            return render(request, "register.html", {'msg': message})

        else:
            if password == cpassword:
                newuser = RegiUser.objects.create(Firstname=fname, Lastname=lname, Email=email, Password=password, receId=receId)

                messages.success(request, 'Your request was successful.')
                return render(request, "login.html")

            else:
                message = "Password and Confirm password are not matched"
                return render(request, "register.html", {'msg': message})


# Login page view

def LoginPage(request):
    return render(request, "login.html")


def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = RegiUser.objects.get(Email=email)

            if user.Password == password:
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['receId'] = user.Lastname
                request.session['Email'] = user.Email

                return redirect('bpm')
            else:
                message = "Password not match"
                return render(request, "login.html", {'msg': message})

        except RegiUser.DoesNotExist:
            message = "User does not exist"
            return render(request, "login.html", {'msg': message})

    else:
        return render(request, "login.html")



def BPM1(request):
    bpm_list = BPM.objects.all()
    paginator = Paginator(bpm_list, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'bpm.html', context)


def BPM2(request):
    tab = BPM.objects.all()
    s = {'tab': tab}
    return render(request, 'graphe.html', s)


def exp_csv(request):
    obj = BPM.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=BPMtable.csv'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    writer.writerow(['ID', 'BPM', 'DT'])

    studs = obj.values_list('id', 'bpm', 'dt')
    for std in studs:
        writer.writerow(std)
    return response


def PRESSION1(request):
    tab = PRESSION.objects.all()
    paginator = Paginator(tab, 10) # Change 10 to the number of items to display per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pression.html', {'page_obj': page_obj})


def PRESSION2(request):
    tab = PRESSION.objects.all()
    s = {'tab': tab}
    return render(request, 'pgraphe.html', s)


def exp_csv1(request):
    obj = PRESSION.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=PRESSSIONtable.csv'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    writer.writerow(['Systolique', 'Diastolique', 'DT'])

    studs = obj.values_list('systolique', 'diastolique', 'dt')
    for std in studs:
        writer.writerow(std)
    return response


def Temp1(request):
    temps = Temp.objects.all()
    paginator = Paginator(temps, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'temperature.html', {'page_obj': page_obj})


def Temp2(request):
    tab = Temp.objects.all()
    s = {'tab': tab}
    return render(request, 'tgraphe.html', s)


def exp_csv2(request):
    obj = Temp.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=Temperaturetable.csv'
    response.write(u'\ufeff'.encode('utf8'))
    writer = csv.writer(response)
    writer.writerow(['ID', 'TEMP', 'DT'])

    studs = obj.values_list('id', 'temp', 'dt')
    for std in studs:
        writer.writerow(std)
    return response


def readmore(request):
    return render(request, 'read_more.html')