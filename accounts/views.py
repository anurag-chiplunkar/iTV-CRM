from django.shortcuts import render, redirect
from django.forms import ValidationError
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import *
from . models import *
import re


def emp_registration(request):
    form = Employee_registration(request.POST or None)
    context = {"form": form}
    print(request.POST)
    print(form.errors)

    if form.is_valid():
        emp_fname = form.cleaned_data.get('emp_fname')
        emp_lname = form.cleaned_data.get('emp_lname')
        emp_email = form.cleaned_data.get('emp_email')
        emp_phone = form.cleaned_data.get('emp_phone')
        print(type(emp_phone))
        emp_desgn = request.POST.get('jobtitle')
        emp_reporting_mgr = form.cleaned_data.get('emp_reporting_mgr')

        emp_pass1 = form.cleaned_data.get('emp_pass1')
        emp_pass2 = form.cleaned_data.get('emp_pass2')

        flag = 0
        while True:  
            if (len(emp_pass1)<8):
                flag = -1
                break
            elif not re.search("[a-z]", emp_pass1):
                flag = -1
                break
            elif not re.search("[A-Z]", emp_pass1):
                flag = -1
                break
            elif not re.search("[0-9]", emp_pass1):
                flag = -1
                break
            elif not re.search("[_@$]", emp_pass1):
                flag = -1
                break
           
            else:
                flag = 0
                print("Valid Password")
                break
        
        #validations
        if flag ==-1:
            print("Not a Valid Password")
            messages.error(request,"Password should have minimum 8 characters. \
                                    Password should contain atleast one uppercase character.\
                                    Password should contain atleast one lowercase character.\
                                    Password should contain atleast one '@', '_' or '$'\
                                    ")
        
        elif (emp_pass1 != emp_pass2):
            messages.error(request, "Password is not matching")

        elif ('@itvnetwork.com') not in emp_email:
            messages.error(request,"Email id should have '@itvnetwork.com'")

        elif len(emp_phone)<10:
            messages.error(request,"Enter a valid phone number")
        
        #elif type(emp_phone) != int:
            #messages.error(request,"Phone number should only contain numbers")

        else:
            obj = Employees(emp_fname=emp_fname,
                        emp_lname=emp_lname,
                        emp_email=emp_email,
                        emp_phone=emp_phone,
                        emp_desgn=emp_desgn,
                        emp_reporting_mgr=emp_reporting_mgr
                        )

            obj.save()

            # email before the '@' is saved as username in django backend
            myuser = User.objects.create_user(emp_email[:emp_email.find('@')], emp_email, emp_pass1)
            return redirect('/emp_login')
            messages.success(request,"Account successfully created!")

    else:
        print("employee registration form invalid")

    return render(request, 'accounts/emp_registration.html', context)


def emp_login(request):
    form = Employee_login(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        print('login form is valid')
        print(form.cleaned_data)
        email = form.cleaned_data.get('emp_email')
        username = email[:email.find('@')]
        password = form.cleaned_data.get('emp_pass1')

        user = authenticate(request, username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            print(request.user)
            print('You are logged in')
            return redirect('/profile')

            qs1 = Employees.objects.filter(emp_email=email)
            qs_context = {"qs": qs1}

            for i in qs_context['qs']:
                email = i.emp_desgn

            return render(request, 'profiles/profile.html', qs_context)

    return render(request, 'accounts/emp_login.html', context)
