from django.urls import path
from .views import sample_api, account_login

urlpatterns = [
    path('', sample_api, name="api_home"),
    path('/account/login', account_login, name="account_login")
]