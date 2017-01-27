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
    # # 比赛题目细节
    url(
        r'^(?P<contest_id>\d+)/problem/(?P<problem_sort>\d+)/$',
        views.ContestProblemDetailAPIView.as_view(),
        name='contest-problem-detail'
    ),
    # 比赛提交状态(全部)
    url(
        r'^(?P<pk>\d+)/status/$',
        views.ContestStatusAPIView.as_view(),
        name='contest-status'
    ),
    # # 比赛排名
    # url(
    #      r'^(?P<pk>\d+)/ranklist/$',
    #      views.ContestRanklistAPIView.as_view(),
    #      name='contest-ranklist'
    # ),
    # 比赛提交列表(当前用户-全部) [GET:最近提交] POST:需要指定题号]
    url(
        r'^(?P<pk>\d+)/submission/$',
        views.ContestSubmissionListAPIView.as_view(),
        name='contest-submission-list'
    ),
    # 比赛提交状态(当前用户-某道题) [GET:该题最近提交 POST:从URL获取题号]
    url(
        r'^(?P<contest_id>\d+)/submission/(?P<problem_sort>\d+)/$',
        views.ContestProblemSubmissionListAPIView.as_view(),
        name='contest-problem-submission-list'
    ),
]
