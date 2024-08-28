from django.contrib import admin
from django.urls import path
from home.views import *
from home import views


urlpatterns = [
    path("admin/" , admin.site.urls),
    path('', index, name= "index"),
    path("home/", home , name="home"),
    path("about/", about , name="about"),
    path("whyus/", whyus , name="whyus"),
    path("Ourteam/", Ourteam , name="Ourteam"),
    path("Service/", Service , name="Service"),
    path("carrers/", carrers , name="carrers"),
    path("contactus/", contactus , name="contactus"),
    path("buyer/", buyer , name="buyer"),
    path("builder/", builder , name="builder"),
    path("broker/", broker , name="broker"),
    path("experia/", experia , name="experia"),
    path("thebridge/", thebridge, name="thebridge"),
    # path('contact/', contact_view, name='contact'),
    # path('success/', success_view, name='success'),



]