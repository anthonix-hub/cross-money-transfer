from django.urls import path
from hi_hiApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account_info', views.account_info, name='account_info'),
    path('activity', views.activity, name='activity'),
    path('add_to_pot', views.add_to_pot, name='add_to_pot'),
    path('card_added', views.card_added, name='card_added'),
    path('help', views.help, name='help'),
    path('send_money', views.send_money, name='send_money'),
    path('transfer_status', views.transfer_status, name='transfer_status'),
    path('wallet', views.wallet, name='wallet'),
    path('welcome', views.welcome, name='welcome'),
    
    path('dashboard', views.dashboard, name='dashboard'),
    
    path('signup', views.signup, name='signup'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
]
