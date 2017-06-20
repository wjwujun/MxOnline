"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include

from .views import OrgView,AddUserAskView,OrgHomeView

urlpatterns = [

    url(r'^list/', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name='org_home'),



]


















