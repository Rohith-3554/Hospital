from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('booking', views.booking,name='booking'),
    path('bookingdetails', views.bookingdetails,name='bookingdetails'),
    path('doctors', views.doctors,name='doctors'),
    path('contact', views.contact,name='contact'),
    path('register/', views.register, name='register'),
    path('login', views.login_view,name='login'),
    path('logout', views.logout_view,name='logout'),
    path('department', views.department,name='department'),

]
