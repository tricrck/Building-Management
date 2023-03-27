from django.contrib import admin

# Register your models here.


from .models import Building, Apartment, Tenant

admin.site.register(Building)
admin.site.register(Apartment)
admin.site.register(Tenant)