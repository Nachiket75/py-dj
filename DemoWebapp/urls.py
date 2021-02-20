#This file is created to connect the webapp(DemoWebapp) and its content in views.py to website (DJWebsite). thats why name is also same urls.py as urls.py
# in Djwebsite
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('add',views.add,name= "Add")
]


