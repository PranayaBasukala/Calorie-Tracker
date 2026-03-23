from django.urls import path
from . import views
# from .views import get_food_item

urlpatterns = [
    path('', views.SignUpPage, name='signup'),
    path('login/', views.LoginPage, name='login'),   
    path('main/', views.main, name='main'),
    path('logout/', views.logoutpage, name='logout'),
    # path('SignUp', views.handleSignUp, name='handleSignUp'),
    # path('login', views.handleLogin, name='handleLogin'),
  
]