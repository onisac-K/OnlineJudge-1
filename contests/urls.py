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
        name='contest-problem-detail'
    ),
    # 比赛状态(全部提交)
    # TODO: 显示用户最近所有的比赛提交
    url(
        r'^(?P<pk>\d+)/submissions/$',
        views.ContestSubmissionListAPIView.as_view(),
        name='contest-submissions'
    ),
    # 比赛状态细节(显示某提交的代码)
    url(
        r'^(?P<contest_id>\d+)/submission/(?P<submission_id>\d+)/$',
        views.ContestSubmissionDetailAPIView.as_view(),
        name='contest-submission-detail'
    ),
    # 每道题用户自己的提交 [GET:获取 POST:提交]
    url(
        r'^(?P<contest_id>\d+)/problem/(?P<problem_sort>\d+)/submission/$',
        views.ContestProblemSubmissionListAPIView.as_view(),
        name='contest-submission-list'
    ),
    # # 比赛排名
    # url(
    #      r'^(?P<pk>\d+)/ranklist/$',
    #      views.ContestRanklistAPIView.as_view(),
    #      name='contest-ranklist'
    # ),
]
