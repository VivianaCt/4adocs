from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.stock import Stock
from .models.admins import Admin

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Stock)
admin.site.register(Admin)

# Register your models here.
