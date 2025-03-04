"""
URL configuration for project21 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_accessRecordss/',insert_accessRecordss,name='insert_accessRecordss'),
    path('display_topic/',display_topic,name='display_topic'),
    path('display_webpage/',display_webpage,name='display_webpage'),
    path('display_AccessRecords/',display_AccessRecords,name='display_AccessRecords'),
    path('update_Webpage/',update_Webpage,name='update_Webpage'),
    path('delete_webpage/',delete_webpage,name='delete_webpage'),
    path('delete_Book/',delete_Book,name='delete_Book'),

    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('select_multiple/',select_multiple,name='select_multiple'),
    path('checkbox/',checkbox,name='checkbox'),
  
]
