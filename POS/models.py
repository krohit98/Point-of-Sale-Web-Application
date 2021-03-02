from django.db import models
from registrations.models import RestaurantRegistrationTable
from RMS.models import MenuItemsTable
# Create your models here.

orderType = (
    ('dinein','Dine-in'),
    ('delivery','Delivery'),
    ('takeaway','Takeaway'),
)

class CustomerManagementTable(models.Model):
    Restaurant_ID = models.ForeignKey(RestaurantRegistrationTable, on_delete=models.CASCADE)
    Customer_Name = models.CharField(max_length = 30)
    Customer_Phone = models.IntegerField()
    Customer_Order_Count = models.IntegerField()

class OrderItemsTable(models.Model):
    Restaurant_ID = models.ForeignKey(RestaurantRegistrationTable, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey('CustomerManagementTable', on_delete=models.CASCADE)
    Item_ID = models.ForeignKey(MenuItemsTable, on_delete=models.CASCADE)
    Item_Name = models.CharField(max_length = 50)
    Item_Price = models.FloatField()
    Item_Quantity = models.FloatField()
    Discount_Percentage = models.IntegerField()
    Total_Item_Price = models.FloatField()

class OrderManagementTable(models.Model):
    Restaurant_ID = models.ForeignKey(RestaurantRegistrationTable, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey('CustomerManagementTable', on_delete=models.CASCADE)
    Customer_Order_Count = models.IntegerField()
    Items_Ordered = models.CharField(max_length = 500)
    Order_Price = models.FloatField()
    Order_Type = models.CharField(max_length = 20, choices = orderType)
    Number_of_seats = models.IntegerField()
    Table_Number = models.IntegerField()
    Discount_Percentage = models.IntegerField()
    Amount_To_Pay = models.FloatField()
    Amount_Recieved = models.FloatField()
    Balance_Returned = models.FloatField()
    Order_Date = models.DateField(auto_now_add=True)
    Order_Time = models.TimeField(auto_now_add=True)
    Invoice = models.ImageField()
