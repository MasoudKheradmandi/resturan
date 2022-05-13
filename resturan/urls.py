from django.urls import path
from . import views

app_name='resturan'

urlpatterns = [
    path('',views.home , name='home'),
    path('x/',views.contact_us,name='contact'),
    path('details/',views.blog,name='blog_details'),
]