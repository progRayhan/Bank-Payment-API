from django.urls import path
from app_1.api.views import UserListAV, UserDetailAV, BalanceListAV, BalanceDetailAV

urlpatterns = [
    path('userlist', UserListAV.as_view(), name='userlist'),
    path('userdetail', UserDetailAV.as_view(), name='userdetail'),
    path('balancelist', BalanceListAV.as_view(), name='balancelist'),
    path('balancedetail', BalanceDetailAV.as_view(), name='balancedetail'),
]