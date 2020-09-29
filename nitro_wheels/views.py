from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import users
from .models import useractive
from django.contrib.auth.models import User

# Create your views here.
global ids
ids=0
def index(request):
 	return render(request,'nitro_wheels/home.html',{}) 

def login(request):
 	return render(request,'nitro_wheels/login.html',{})
 	
def registration(request):
	return render(request,'nitro_wheels/registration.html',{}) 
 
def dash(request):
	global ids
	print(ids)
	b=users.objects.all()
	for i in b:
		if i.id==ids:
			return render(request,'nitro_wheels/dashboard.html',{'name':i.name,'dob':i.dob,
				'email':i.email,'usrname':i.usrname,'number':i.contact,'add':i.address,
				'status':i.status,'datab':i.profile_pic})

def logout(request):
	return render(request,'nitro_wheels/logout.html',{}) 

def edit(request):
	print(ids)
	# return render(request,'nitro_wheels/form.html',{}) 
	return render(request,'nitro_wheels/profile_edit.html',{}) 


def order_bike(request):
	global ids
	print(ids)
	b=users.objects.all()
	for i in b:
		if i.id==ids:
			return render(request,'nitro_wheels/order1.html',{'name':i.name,'usrname':i.usrname,'datab':i.profile_pic})

def order_rep(request):
	global ids
	print(ids)
	b=users.objects.all()
	for i in b:
		if i.id==ids:
			return render(request,'nitro_wheels/order3.html',{'name':i.name,'usrname':i.usrname,'datab':i.profile_pic})
#computer start#	
def harleyDavidson(request):
	global ids
	print(ids)
	b=users.objects.all()
	for i in b:
		if i.id==ids:
			return render(request,'nitro_wheels/order11.html',{'name':i.name,'usrname':i.usrname,'datab':i.profile_pic})

def yamaha(request):
	global ids
	print(ids)
	b=users.objects.all()
	for i in b:
		if i.id==ids:
			return render(request,'nitro_wheels/order12.html',{'name':i.name,'usrname':i.usrname,'datab':i.profile_pic})
def gb(request):
	global ids
	print(ids)
	b=users.objects.all()
	for i in b:
		if i.id==ids:
			return render(request,'nitro_wheels/order31.html',{'name':i.name,'usrname':i.usrname,'datab':i.profile_pic})
def en(request):
	global ids
	print(ids)
	b=users.objects.all()
	for i in b:
		if i.id==ids:
			return render(request,'nitro_wheels/order32.html',{'name':i.name,'usrname':i.usrname,'datab':i.profile_pic})
def sp(request):
	global ids
	print(ids)
	b=users.objects.all()
	for i in b:
		if i.id==ids:
			return render(request,'nitro_wheels/order33.html',{'name':i.name,'usrname':i.usrname,'datab':i.profile_pic})

#repair end#


@csrf_exempt
def edit_data(request):
	print(ids,'hello')
	if(request.POST):
		print(request.POST)
		name=request.POST.get('name')
		usrname='@'
		usrname+=request.POST.get('usrname')
		ussrname=request.POST.get('usrname')
		email=request.POST.get('email')
		contact=request.POST.get('contact')
		months=request.POST.get('months')
		dates=request.POST.get('dates')
		years=request.POST.get('years')
		dob=''
		dob=dates+'.'+months+'.'+years
		address=request.POST.get('address')
		status=request.POST.get('status')

		if(name!=""):
			users.objects.filter(id=ids).update(name=name)
		if(ussrname!=""):
			users.objects.filter(id=ids).update(usrname=usrname)
		if(email!=""):
			users.objects.filter(id=ids).update(email=email)
		if(dob!=""):
			users.objects.filter(id=ids).update(dob=dob)
		if(contact!=""):
			users.objects.filter(id=ids).update(contact=contact)
		if(address!=""):
			users.objects.filter(id=ids).update(address=address)
		if(status!=""):
			users.objects.filter(id=ids).update(status=status)
	return HttpResponse('success')





@csrf_exempt
def data(request):
	if(request.POST):
		print(request.POST)
		name=request.POST.get('name')
		months=request.POST.get('months')
		dates=request.POST.get('dates')
		years=request.POST.get('years')
		dob=''
		dob=dates+'.'+months+'.'+years
		# dob=request.POST.get('dob')
		email=request.POST.get('email')
		usrname='@'
		usrname+=request.POST.get('usrname')
		passw=request.POST.get('pass')
		input1=users.objects.create(name=name,dob=dob,email=email,usrname=usrname,password=passw,profile_pic='NA',contact='NA',address='NA',status='NA')
	return HttpResponse('success')

@csrf_exempt
def get_data(request):
	k=0 
	if(request.POST):
		print(request.POST)
		usrname='@'
		usrname+=request.POST.get('usrname')
		passw=request.POST.get('pass')
		print(usrname)
		for j in users.objects.all():
			if(usrname==j.usrname and passw==j.password):
				print('match')
				k=1
				global ids
				ids=j.id
				# useractive.objects.filter(id=1).update(userid=j.id)
				break;

	if(k==1):
		print(ids)
		return HttpResponse('success')
	if(k==0):
		return HttpResponse('no')
