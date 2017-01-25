from django.conf.urls import url#, include
# from rest_framework.routers import DefaultRouter

from contests import views

# router = DefaultRouter()
# router.register(r'', views.ContestViewSet)

urlpatterns = [
    url(r'^$', views.ContestListAPIView.as_view(), name='contest-list'),
    url(r'^(?P<pk>\d+)/$', views.ContestDetailAPIView.as_view(), name='contest-detail'),
    url(r'^(?P<contest_id>\d+)/problem/(?P<problem_sort>\d+)/$', views.ContestProblemDetailAPIView.as_view(), name='contestproblem-detail'),

    # url(r'^', include(router.urls)),
    # url(r'^$', ProblemListAPIView.as_view(), name='problem-list'),
    # url(r'^(?P<pk>\d+)/$', ProblemDetailAPIView.as_view(), name='problem-detail'),
]
