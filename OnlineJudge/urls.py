"""OnlineJudge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

# from rest_framework.urlpatterns import format_suffix_patterns

# views
from .views import api_root
import profiles

urlpatterns = [
    # API ROOT
    url(r'^$', api_root, name='api-root'),

    # 管理员
    url(r'^admin/', admin.site.urls, name='admin'),

    # Profile 相关
    url(r'^profile/', include('profiles.urls')),
    url(r'^ranklist/$', profiles.views.RanklistAPIView.as_view(), name='ranklist'),
    url(r'^register/$', profiles.views.SignUpAPIView.as_view(), name='sign-up'),

    # Problem 相关
    url(r'^problem/', include('problems.urls')),

    # Contest 相关
    url(r'^contest/', include('contests.urls')),
]

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^', include('rest_framework.urls', namespace='rest_framework')),
]
