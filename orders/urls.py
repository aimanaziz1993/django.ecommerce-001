from django.urls import path, include

from orders import views


urlpatterns = [

    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.OrdersList.as_view())

]