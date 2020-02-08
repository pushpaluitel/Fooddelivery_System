from django.shortcuts import render
from delivery.models import Customer, Menu
from delivery.forms import customerform, menuform

def home(request):
	return render(request, "index.html")

def menu(request):
	return render(request, "menu.html")
	
def faq(request):
	return render(request, "FAQs.html")
	
def login(request):
	return render(request, "login.html")
	
def order(request):
	return render(request, "order.html")

def about(request):
	return render(request, "aboutus.html")
	
def signup(request):
	if request.method == 'POST':
		if request.POST.get('First_Name') and request.POST.get('Last_Name') and request.POST.get('Email') \
				and request.POST.get('Password1') and request.POST.get('Gender') and request.POST.get('DOB'):
			cus= Customer()
            cus.First_Name = request.POST.get('First_Name')
            cus.Last_Name = request.POST.get('Last_Name')
            cus.Email = request.POST.get('Email')
            cus.Password = request.POST.get('Password1')
            cus.Gender = request.POST.get('Gender')
            cus.DOB = request.POST.get('DOB')
            cus.save()
		return render(request,'login.html')
	else:
		return render(request, 'signup.html)


def dashboard_menu(request):
	menus = Menu.objects.all()
	return render(request, "dashboard_menu.html",{'menus':menus})