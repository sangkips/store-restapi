from django.contrib import admin

from store.models import Customer, Order


admin.site.register(Customer)
admin.site.register(Order)

