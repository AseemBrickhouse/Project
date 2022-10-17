from django.urls import path, include
from django.conf.urls import url
from backend.AllViews.AccountViews import *

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('AccountCreation/', AccountCreation.as_view()),
    path('CurrentUser/', CurrentUser.as_view()),
]