from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bank import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('accounts/', views.AccountList.as_view()),
    path('depos/', views.DepositList.as_view()),
    path('depos/<int:pk>/', views.DepositDetail.as_view()),
    path('withdrawals/', views.WithdrawList.as_view()),
    path('withdrawals/<int:pk>/', views.WithdrawDetail.as_view()),
    path('accounts/<int:pk>/', views.AccountDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)