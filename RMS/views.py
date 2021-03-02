from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from registrations.models import *
from RMS.models import*
from POS.models import*

# Create your views here.
def adminProfile(request):
    restDetails = RestaurantRegistrationTable.objects.filter(user_id=request.user.id)
    adminDetails = User.objects.filter(username = request.user.username)
    return render(request,'adminPage.html',{'details':restDetails, 'Adetails':adminDetails})

def managerProfile(request):
    manager = ManagerRegistrationTable.objects.filter(user_id = request.user.id)
    Manager_AccessID = manager[0].Manager_AccessID
    Restaurant_ID = manager[0].Restaurant_id
    restDetails = RestaurantRegistrationTable.objects.filter(user_id=Restaurant_ID)
    managerDetails = User.objects.filter(username = request.user.username)
    toPass = {'Restaurantdetails':restDetails,'Managerdetails':managerDetails,'Manager_AccessID':Manager_AccessID}
    return render(request,'managerPage.html', toPass)

def logout(request):
    auth.logout(request)
    return redirect('/')