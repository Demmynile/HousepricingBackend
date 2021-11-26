from django.urls import path , include
from .views import HousepricingView




urlpatterns = [
    path('houseprice/' , HousepricingView.as_view() , name = 'house_pricing')
]



