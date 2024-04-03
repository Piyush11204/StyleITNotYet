from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  
   path("", views.index, name='home'),
   path("home",views.index, name= 'home'),
   path("signin",views.signin, name= 'signin'),
   path("sign_up",views.sign_up, name= 'sign_up'), 
   path("signout",views.signout, name= 'signout'),
   path("about", views.about, name='about'),
   path("cart", views.cart, name='cart'),
   path("add", views.add, name='add'),
   path("contact", views.contact, name='contact'),
   path("recently", views.recently, name='recently'),
   path("activate/<uidb64>/<token>", views.activate, name='activate'),
   path("footer", views.footer, name='footer'),
   path("products", views.products, name='products'),
   path("product_page", views.product_page, name='product_page'),
   path("admin/", views.admin, name='admin'),
   path("reset_password/", auth_views.PasswordResetView.as_view(), name='reset_password'),
   path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="reset_password_done"),
   path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm_view'),
   path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="reset_password_complete"),
   ] 