"""ClassBasedViews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from cbv_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'), #fbv
    path('cbv/',views.indexview.as_view(),name='index'),
    path('temp1fbv/',views.temp1,name='temp1'),
    path('temp1cbv/',views.TemplateDemoView.as_view(),name='templatedemoview'),
    path('fbvform/',views.FBV_Backend,name='temp2'),
    path('cbvform/',views.Form_Demo.as_view(),name='temp2'),
    path('base/',views.TempView.as_view()),
    path('cbv_app/',include("cbv_app.urls")),

]
