from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Courier)
admin.site.register(Address)
admin.site.register(CustomerSupport)


