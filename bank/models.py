from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateTimeField

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Accounts(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    acc_balance = models.DecimalField(max_digits=15, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.owner

class Deposit(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateTimeField(auto_now_add = True)        

class Withdraw(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateTimeField(auto_now_add = True)   

class Transfer(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateTimeField(auto_now_add = True)   