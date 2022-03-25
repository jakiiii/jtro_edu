from django.urls import path
from apps.payment.views import PricingView

app_name = 'payment'


urlpatterns = [
    path('', PricingView.as_view(), name='pricing'),
]
