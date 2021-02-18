"""DjWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# pip install django
# django-admin startproject DjWebsite using this command we create django project
# python manage.py runserver to run server to see server open browser go to url http://127.0.0.1:8000/
# you can execute command ctrl+c  the execution after you open url
# python manage.py startapp DemoWebapp it will create webapplication (website contains many webapplications)
# python manage.py migrate this command is used to connect django with already existing database sqlite

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('DemoWebapp.urls'))
]
