from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bank.permissions import IsOwnerOrReadOnly
from .serializers import *
from .models import  *
from django.contrib.auth.models import User

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AccountList(generics.ListCreateAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accounts.objects.all()
    serializer_class = AccountSerializer       
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class DepositList(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer 

class DepositDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer   

@api_view(['GET', 'POST'])
def deposit(request):
    serializer = DepositSerializer(data=request.data)

    data = serializer.validated_data
    amount = data["amount"]

    balance = data.account.acc_balance - amount

    if serializer.is_valid():
        serializer.save()

    return Response({'balance': balance})   