from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from .forms import OrderForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
# Create your views here.

def login(request):
	if request.session.has_key('is_logged'):
		return redirect('home')
	if request.POST:
		email = request.POST['email']
		password = request.POST['password']
		count=User.objects.filter(email=email,password=password).count()
		if count > 0:
			request.session['is_logged'] = True
			return redirect('home')
		else:
			messages.error(request,'You are enter invalid credentials')
			return redirect('login')
	return render(request,'accounts/login.html')

def signup(request):
	return render(request,'accounts/signup.html')

def register_user(request):
	if request.POST:
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		obj = User(username=username,email=email,password=password)
		obj.save()
		messages.success(request,'You are successfully Registered')
		return redirect('login')
	return HttpResponse('Invalid Credentials')

def handlelogout(request):
	if request.session.has_key('is_logged'):
		del request.session['is_logged']
		return redirect('login')
	else:
		return redirect('login')


# @login_required(login_url='/login/')
def home(request):
	if request.session.has_key('is_logged'):
		orders = Order.objects.all()
		customers = Customer.objects.all()

		total_customers = customers.count()

		total_orders = orders.count()
		delivered = orders.filter(status='Delivered').count()
		pending = orders.filter(status='Pending').count()

		context = {'orders':orders, 'customers':customers,'total_orders':total_orders,'delivered':delivered,'pending':pending }
		messages.success(request,'You are successfully Logged In')
		return render(request, 'accounts/dashboard.html', context)
	return redirect('login')
# @login_required(login_url='/login/')
# 
def products(request):
	if request.session.has_key('is_logged'):
		products = Product.objects.all()
		return render(request,'accounts/products.html', {'products':products})
	return redirect('login')

# @login_required(login_url='login')

def customers(request, pk_test):
	if request.session.has_key('is_logged'):
		customer = Customer.objects.get(id=pk_test)

		orders = customer.order_set.all()
		order_count = orders.count()

		context = {'customer':customer, 'orders':orders, 'order_count':order_count}
		return render(request, 'accounts/customer.html',context)
	return redirect('login')
# def customers(request):

#     return render(request,'accounts/customer.html')
# @login_required(login_url='/login/')

def createOrder(request):
	if request.session.has_key('is_logged'):

		form = OrderForm()
		if request.method == 'POST':
			#print('Printing POST:', request.POST)
			form = OrderForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/')

		context = {'form':form}
		return render(request, 'accounts/order_form.html', context)
	return redirect('login')

# @login_required(login_url='/login/')

def updateOrder(request, pk):
	if request.session.has_key('is_logged'):

		order = Order.objects.get(id=pk)
		form = OrderForm(instance=order)

		if request.method == 'POST':
			form = OrderForm(request.POST, instance=order)
			if form.is_valid():
				form.save()
				return redirect('/')

		context = {'form':form}
		return render(request, 'accounts/order_form.html', context)
	return redirect('login')

# @login_required(login_url='/login/')

def deleteOrder(request, pk):
	if request.session.has_key('is_logged'):
		order = Order.objects.get(id=pk)
		if request.method == "POST":
			order.delete()
			return redirect('/')

		context = {'item':order}
		return render(request, 'accounts/delete.html', context)
	return redirect('login')




