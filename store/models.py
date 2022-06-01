from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    ordered_item = models.CharField(max_length=155)
    date_ordered = models.DateTimeField(auto_now_add=True)
    item_amount = models.FloatField()

    def __str__(self):
        return self.ordered_item
