from django.conf.urls import url, include
from django.contrib import admin

from profiles.views import UserProfileAPIView

urlpatterns = [
    url(r'^(?P<username>\w*)/?$', UserProfileAPIView.as_view(), name='user-detail'),
]
