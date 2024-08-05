from django.urls import path
from site_app.views.index import *
from site_app.views.order import OrderCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('orders/', OrderCreateView.as_view(), name='create_order')
]
