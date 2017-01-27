from django.conf.urls import url#, include
# from rest_framework.routers import DefaultRouter

# from problems.views import ProblemListAPIView, ProblemDetailAPIView
from problems import views

# router = DefaultRouter()
# router.register(r'', views.ProblemViewSet)

urlpatterns = [
    url(r'^$', views.ProblemListAPIView.as_view(), name='problem-list'),
    url(r'^(?P<pk>\d+)/$',views.ProblemDetailAPIView.as_view(), name='problem-detail'),
    url(r'^(?P<pk>\d+)/submit/$', views.ProblemSubmitAPIView.as_view(), name='problem-submit'),
]
