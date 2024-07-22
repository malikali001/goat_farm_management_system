from django.urls import path
from .views import dashboard
from django.conf.urls import handler500
from base.views import custom_error_view

handler500 = custom_error_view

urlpatterns = [
    path('', dashboard.as_view(), name='dashboard'),
]
