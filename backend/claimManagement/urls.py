from django.urls import path 
from .views import CustomerSearchView,ReactView
urlpatterns = [
    path('search/', CustomerSearchView.as_view(), name="search" ),
    path('data/', ReactView.as_view(), name="data")
]