from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from registrations.models import RestaurantRegistrationTable

# Create your views here.
def index(request):
    return render(request, 'index.html')

def authManager(request):
    return render(request, 'AuthorizeManager.html')

def authStaff(request):
    return render(request,'AuthorizeStaff.html')

def loginManager(request):
    return render(request, 'ManagerLogin.html')

def loginStaff(request):
    return render(request, 'StaffLogin.html')

def registerAdmin(request):
    if request.method=='POST':
        adminName=request.POST['adminName']
        nameArr=adminName.split(" ");
        adminFirstName=nameArr[0];
        adminLastName=nameArr[1];
        adminEmail=request.POST['adminEmail']
        adminAddress=request.POST['adminAddress']
        adminContact=request.POST['adminContact']
        restaurantName=request.POST['restaurantName']
        restaurantAddress=request.POST['restaurantAddress']
        adminAccessID=request.POST['adminAccessID']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if registrations_user.objects.filter(email=email).exists():
                messages.info(request,'email already in use')
                return redirect('registerAdmin')
            else:
                user=restaurant_user.objects.create_user(username=email, password=password1, email=email, first_name=AdminFirstName, last_name=AdminLastName, address=adminAddress, contact=adminContact)
                restaurant=RestaurantRegistrationTable.objects.create_user(user=user, Restaurant_name=restaurantName, Restaurant_address=restaurantAddress, Admin_AccessID=adminAccessID)
                user.save()
                restaurant.save()
                return redirect('/')

    else:
        return render(request, 'RegisterAdmin.html')

def loginAdmin(request):
    return render(request, 'AdminLogin.html')