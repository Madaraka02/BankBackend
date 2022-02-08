from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'account']


class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')       
    bank = serializers.ReadOnlyField(source='bank.name')  

    class Meta:
        model = Accounts
        fields = ['id', 'owner', 'bank', 'acc_balance', 'date_created'] 


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        mode = Deposit
        fields = ['id', 'amount', 'account', 'transaction_date']


class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        mode = Withdraw
        fields = ['id', 'amount', 'account', 'transaction_date']


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        mode = Transfer
        fields = ['id', 'amount', 'account', 'transaction_date']

