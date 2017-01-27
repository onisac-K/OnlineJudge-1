from django.conf.urls import url

from contests import views

urlpatterns = [
    # 比赛列表
    url(
        r'^$',
        views.ContestListAPIView.as_view(),
        name='contest-list'
    ),
    # 比赛细节 即比赛题目列表
    url(
        r'^(?P<pk>\d+)/$',
        views.ContestDetailAPIView.as_view(),
        name='contest-detail'
    ),
    # 比赛题目细节
    url(
        r'^(?P<contest_id>\d+)/problem/(?P<problem_sort>\d+)/$',
        views.ContestProblemDetailAPIView.as_view(),
        name='contestproblem-detail'
    ),
]
