from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("signup",views.signup,name='signup'),
    path("app",views.app,name="app"),
    path('login',views.loginA,name="login")
]
