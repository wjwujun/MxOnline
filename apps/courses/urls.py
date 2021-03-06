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

from .views import CourseListView,CourseDetaileView,CourseInfoView


urlpatterns = [

    #课程列表页
    url(r'^list/', CourseListView.as_view(), name="course_list"),

    #课程详情页
    url(r'^detaile/(?P<course_id>\d+)/', CourseDetaileView.as_view(), name="course_detaile"),

    #
    url(r'^info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name="course_video"),



]


















