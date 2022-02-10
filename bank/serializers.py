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
    account = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source='account.owner.username')
    balance = serializers.ReadOnlyField ()
    class Meta:
        model = Deposit
        fields = ['id', 'amount', 'account', 'transaction_date', 'balance']


class WithdrawSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source='account.owner.username')
    balance = serializers.ReadOnlyField ()
    class Meta:
        model = Withdraw
        fields = ['id', 'amount', 'account', 'transaction_date', 'balance']


class TransferSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(many=False, read_only=True, source='account.owner.username')
    balance = serializers.ReadOnlyField ()
    class Meta:
        model = Transfer
        fields = ['id', 'amount', 'account', 'transaction_date', 'balance']

