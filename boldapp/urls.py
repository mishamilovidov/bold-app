"""boldapp URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_user, name='logout'),
    url(r'^equipment/$', views.equipment, name='logout'),
    url(r'^equipment_unit/add/$', views.equipment_unit, name='new_equipment'),
    url(r'^equipment_unit/(?P<equipmentid>\d+)/$', views.equipment_unit, name='update_equipment'),
    url(r'^users/', views.users, name='users'),
    url(r'^user/add/', views.user, name='new_user'),
    url(r'^user/(?P<userid>\d+)/$', views.user, name='update_user'),
    url(r'^departments/', views.departments, name='departments'),
    url(r'^department/add/', views.department, name='new_department'),
    url(r'^department/(?P<departmentid>\d+)/$', views.department, name='update_department'),
    url(r'^manufacturers/', views.manufacturers, name='manufacturers'),
    url(r'^manufacturer/add/', views.manufacturer, name='new_manufacturer'),
    url(r'^manufacturer/(?P<manufacturerid>\d+)/$', views.manufacturer, name='update_manufacturer'),
]
