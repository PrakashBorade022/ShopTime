from django.contrib import admin
from .models import  Product,MyCart,MyOrdersNew,Review,Rating


admin.site.register(Product)
admin.site.register(MyCart)
admin.site.register(MyOrdersNew)
admin.site.register(Review)
admin.site.register(Rating)

# Register your models here.
