from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

# from problems.views import ProblemListAPIView, ProblemDetailAPIView
from problems import views

router = DefaultRouter()
router.register(r'', views.ProblemViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^$', ProblemListAPIView.as_view(), name='problem-list'),
    # url(r'^(?P<pk>\d+)/$', ProblemDetailAPIView.as_view(), name='problem-detail'),
]
