
from django.urls import path
from helplessapp import views
urlpatterns = [
  
    path('',views.home,name="home"),
    path('About/',views.About,name="about"),
    path('Donate/',views.Donate,name="donate"),
    path('Gallery/',views.Gallery,name="gallery"),
    path('Sponserroom/',views.Sponserroom,name="sponserroom"),

]  
