from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('/download_section',views.download_section,name="download_section"),
    path('/login',views.login,name="signup"),
    path('/register',views.register,name = "register")


]