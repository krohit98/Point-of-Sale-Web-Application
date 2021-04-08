from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from registrations.models import *
from RMS.models import*
from POS.models import*
from django.http import JsonResponse
from django.http import HttpResponse
from datetime import date, datetime
import json

# Create your views here.
def staffProfile(request):
    staff = StaffRegistrationTable.objects.filter(user_id = request.user.id)
    Restaurant_ID = staff[0].Restaurant_id
    restDetails = RestaurantRegistrationTable.objects.filter(user_id=Restaurant_ID)
    staffDetails = User.objects.filter(username = request.user.username)
    toPass = {'Restaurantdetails':restDetails,'Staffdetails':staffDetails}
    return render(request, 'staffPage.html', toPass)

def takeOrder(request):
    staff = StaffRegistrationTable.objects.filter(user_id = request.user.id)
    Restaurant_ID = staff[0].Restaurant_id
    if request.method == 'POST':
        recievedData = json.loads(request.body)
        itemName = recievedData.get('itemName')
        itemQuantity = float(recievedData.get('itemQuantity'))
        itemDiscount = float(recievedData.get('itemDiscount'))
        customerId = recievedData.get('customerId')
        item = MenuItemsTable.objects.filter(Restaurant_id = Restaurant_ID).filter(Item_Name = itemName)[0]
        order = OrderItemsTable()
        order.Item_Name = itemName
        order.Item_Quantity = itemQuantity
        order.Discount_Percentage = itemDiscount
        order.Item_Price = item.Selling_Price
        discount = ((itemDiscount/100)*item.Selling_Price)*itemQuantity
        totalItemPrice = (item.Selling_Price * itemQuantity) - discount
        order.Total_Item_Price = round(totalItemPrice,2)
        order.Item_id = item.id
        order.Customer_id = customerId
        order.Restaurant_id = Restaurant_ID
        order.save()

    return HttpResponse()

def getOrder(request):
    staff = StaffRegistrationTable.objects.filter(user_id = request.user.id)
    Restaurant_ID = staff[0].Restaurant_id
    if request.method == 'GET':
        itemList = {}
        customerId = request.GET['customerId']
        order = OrderItemsTable.objects.filter(Restaurant_id = Restaurant_ID).filter(Customer_id = customerId)
        for item in order:
            itemList[item.Item_id] = [item.Item_Name, item.Item_Quantity, item.Total_Item_Price]
        return JsonResponse({'itemList':itemList})
    return HttpResponse()

def deleteOrder(request):
    staff = StaffRegistrationTable.objects.filter(user_id = request.user.id)
    Restaurant_ID = staff[0].Restaurant_id
    if request.method == 'GET':
        customerId = request.GET['customerId']
        order = OrderItemsTable.objects.filter(Restaurant_id = Restaurant_ID).filter(Customer_id = customerId)
        if order.exists():
            order.delete()
        customer = CustomerManagementTable.objects.filter(Restaurant_id = Restaurant_ID).filter(id = customerId)
        if customer.exists() and customer[0].Customer_Order_Count == 1:
            customer.delete()
        else:
            customer.update(Customer_Order_Count = customer[0].Customer_Order_Count - 1 )
    return HttpResponse()

def manageOrders(request):
    staff = StaffRegistrationTable.objects.filter(user_id = request.user.id)
    Restaurant_ID = staff[0].Restaurant_id
    restDetails = RestaurantRegistrationTable.objects.filter(user_id=Restaurant_ID)
    toPass = {'Restaurantdetails':restDetails}
    return render(request,"manageOrders.html", toPass)

def manageKOTS(request):
    staff = StaffRegistrationTable.objects.filter(user_id = request.user.id)
    Restaurant_ID = staff[0].Restaurant_id
    today = date.today()
    now = datetime.now()
    if request.method == 'POST':
        recievedData = json.loads(request.body)
        customerId = recievedData.get('customerId')
        orderType = recievedData.get('orderType')
        seatsRequired = recievedData.get('seatsRequired')
        tableNumber = recievedData.get('tableNumber')
        orderDiscount = recievedData.get('orderDiscount')
        amountToPay = recievedData.get('totalPrice')
        amountRecieved = recievedData.get('amountRecieved')
        returnBalance = recievedData.get('returnBalance')
        customer = CustomerManagementTable.objects.filter(Restaurant_id = Restaurant_ID).filter(id = customerId)
        orderCount = customer[0].Customer_Order_Count
        order = OrderItemsTable.objects.filter(Restaurant_id = Restaurant_ID).filter(Customer_id = customerId)
        totalPrice = 0
        orderItems = ""
        for item in order:
            totalPrice += item.Total_Item_Price 
            orderItems += "("+str(item.Item_Name)+" X "+str(int(item.Item_Quantity))+")"
        placedOrder = OrderManagementTable()
        placedOrder.Customer_Order_Count = orderCount
        placedOrder.Items_Ordered = orderItems
        placedOrder.Order_Price = totalPrice
        placedOrder.Order_Type = orderType
        placedOrder.Number_of_seats = seatsRequired
        placedOrder.Table_Number = tableNumber
        placedOrder.Discount_Percentage = orderDiscount
        placedOrder.Amount_To_Pay = amountToPay
        placedOrder.Amount_Recieved = amountRecieved
        placedOrder.Balance_Returned = returnBalance
        placedOrder.Order_Date = today.strftime("%d/%m/%Y")
        placedOrder.Order_Time = now.strftime("%H:%M:%S")
        placedOrder.Invoice = ""
        placedOrder.Customer_id = customerId
        placedOrder.Restaurant_id = Restaurant_ID
        placedOrder.save()

    restDetails = RestaurantRegistrationTable.objects.filter(user_id=Restaurant_ID)
    toPass = {'Restaurantdetails':restDetails}
    return render(request,"manageKOTS.html", toPass)

def manageCustomers(request):
    staff = StaffRegistrationTable.objects.filter(user_id = request.user.id)
    Restaurant_ID = staff[0].Restaurant_id
    if request.method == 'POST':
        recievedData = json.loads(request.body)
        customerName = recievedData.get('customerName').title()
        customerPhone = int(recievedData.get('customerPhone'))
        customerId=0
        customer = CustomerManagementTable.objects.filter(Customer_Name = customerName)
        if customer.exists() and customer[0].Customer_Phone == customerPhone:
                oldCustomer = customer.filter(Customer_Phone = customerPhone)
                oldCustomer.update(Customer_Order_Count = oldCustomer[0].Customer_Order_Count + 1 )
                customerId = oldCustomer[0].id
        else:
            newCustomer = CustomerManagementTable()
            newCustomer.Customer_Name = customerName
            newCustomer.Customer_Phone = customerPhone
            newCustomer.Customer_Order_Count = 1
            newCustomer.Restaurant_id = Restaurant_ID
            newCustomer.save()
            customerId = newCustomer.id
        return JsonResponse({'customerId':customerId})
    
    customerDetails = CustomerManagementTable.objects.filter(Restaurant_id=Restaurant_ID)
    restDetails = RestaurantRegistrationTable.objects.filter(user_id=Restaurant_ID)
    toPass = {'Restaurantdetails':restDetails,'Customerdetails':customerDetails}
    return render(request,"manageCustomers.html", toPass)

def logout(request):
    auth.logout(request)
    return redirect('/')
