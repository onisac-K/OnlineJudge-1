from django.conf.urls import url

from contests import views

urlpatterns = [
    url(
        r'^$',
        views.ContestListAPIView.as_view(),
        name='contest-list'
    ),
    url(
        r'^(?P<pk>\d+)/$',
        views.ContestDetailAPIView.as_view(),
        name='contest-detail'
    ),
    url(
        r'^(?P<contest_id>\d+)/problem/(?P<problem_sort>\d+)/$',
        views.ContestProblemDetailAPIView.as_view(),
        name='contestproblem-detail'
    ),
]
