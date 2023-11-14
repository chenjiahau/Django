from django.contrib import admin
from .models import Address, Country, User, Todo

# Register your models here.

admin.site.register(Address)
admin.site.register(Country)
admin.site.register(User)
admin.site.register(Todo)
