"""SearchAndNav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    #适用于一级的url
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    通过path将根路径为url的访问都分发给某个app去处理
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    #适用与分类的url
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SearchAndNavAPP.views import views

#这里是直接使用Function views，没必要使用二级url
urlpatterns = [
    path('', views.search),
    path('search_simple', views.search_simple),
    path('nav', views.nav),
    path('click_number',views.get_click_number),
    path('click_awesome',views.get_click_awesome),
    path('suggest_search',views.get_suggest_search),
    path('suggest_movie', views.get_suggest_movie),
    path('suggest_book', views.get_suggest_book),
    path('admin/', admin.site.urls),
]
