from django.contrib import admin
from .models import *




# Register your models here.
admin.site.register(Bank)
admin.site.register(Deposit)
admin.site.register(Accounts)
admin.site.register(Withdraw)
admin.site.register(Transfer)


