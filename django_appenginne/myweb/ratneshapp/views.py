from django.shortcuts import render
from flask import Flask, render_template
import datetime as dt
from ratneshapp.myform import LogonForm, LoginForm
from ratneshapp.models import Register
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

def index(request):
	today =  dt.datetime.now()
	return render(request,"template/index.html",{"today":today})
	
#def crudops(request):
#	#Creating an entry
#	
#	register = Register(
#		website = "www.polo.com", mail = "reeya@polo.com", 
#		name = "reeya", phonenumber = "002376970"
#	)
#	
#	register.save()
#	
#	#Read ALL entries
#	objects = Register.objects.all()
#	res ='Printing all Register entries in the DB : <br>'
#	
#	for elt in objects:
#		res += elt.name+"<br>"
#	
#	#Read a specific entry:
#	reeya = Register.objects.get(name = "reeya")
#	res += 'Printing One entry <br>'
#	res += reeya.name
#	
#	#Delete an entry
#	res += '<br> Deleting an entry <br>'
#	reeya.delete()
#	
#	#Update
#	register = Register(
#		website = "www.polo.com", mail = "reeya@polo.com", 
#		name = "reeya", phonenumber = "002376970"
#	)
#	
#	register.save()
#	res += 'Updating entry<br>'
#	
#	register = Register.objects.get(name = 'reeya')
#	register.name = 'thierry'
#	register.save()
#	
#	return HttpResponse(res)
def login(request):
    obj = Register
    log = False
#    print(request.method)	
    if request.method == 'POST':
        MyLoginForm = LoginForm(data=request.POST)
        #print(MyLoginForm,MyLoginForm.errors, type(MyLoginForm.errors))
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['user']
            password = MyLoginForm.cleaned_data['password']
            try:
                name = Register.objects.get(user = username)
                pwd = name.password
                print(name,pwd)
                if(password==pwd):
                    obj = name	
                    log = True	
            except:
                 obj = Register               
    else:
        MyLoginForm = LoginForm()
        
    if(log):
        return render(request, 'template/loggedin.html', {"username" : obj})	
    else:
        return render(request, 'template/saved.html', {"username" : "Invalid user/password"})	
        
#def datamanipulation(request):
#	res = ''
##Filtering data:
#	qs = Register.objects.filter(name="paul")
#	res += "Found : %s results<br>"%len(qs)
#	#Ordering results
#	qs = Register.objects.order_by("name")
#	for elt in qs:
#		res += elt.name + '<br>'
#	return HttpResponse(res)

def SaveLogonForm(request):
    saved = False
    if request.method == "POST":
#Get the posted form
        MyLogonForm = LogonForm(request.POST, request.FILES)
        print(MyLogonForm.is_valid(),MyLogonForm.errors)
        if MyLogonForm.is_valid():
            profile = Register()
            s = profile.user = MyLogonForm.cleaned_data["user"]
            profile.mail = MyLogonForm.cleaned_data["mail"]
            profile.phonenumber = MyLogonForm.cleaned_data["phonenumber"]
            profile.password = MyLogonForm.cleaned_data["password"]
            profile.picture = MyLogonForm.cleaned_data["picture"]
            profile.save()
            saved = True
        else:
            MyLogonForm = LogonForm()
    return render(request, 'template/saved.html', locals())	
