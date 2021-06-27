from django.urls import path
from .import views

urlpatterns = [
    path('Register',views.Register,name="Register"),
    path('login_request',views.login_request,name="login_request"),
    path('',views.store, name="store"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
]