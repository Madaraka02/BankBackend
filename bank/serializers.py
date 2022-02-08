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

    class Meta:
        model = Accounts
        fields = ['id', 'owner', 'bank', 'acc_balance', 'date_created'] 