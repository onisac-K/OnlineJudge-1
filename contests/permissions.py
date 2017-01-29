from rest_framework import permissions
from rest_framework.compat import is_authenticated

from contests.models import Contest


# 进入比赛
# [Public] 无限制
# [Private] 只有注册了比赛的用户可以进入
class IsParticipantOrAdminOrDeny(permissions.BasePermission):

    def has_permission(self, request, view):
        contest = Contest.objects.get(pk=view.kwargs['pk'])
        if contest.public:
            return True
        return request.user.contest_account.filter(contest=contest)


# 比赛提交 - 只允许作者或管理员访问提交细节
class IsAuthorOrAdminOrDeny(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.submission.author == request.user or request.user.is_staff


# 参加比赛
# [Public] 登录而未注册比赛的用户 才允许注册
# [Private] 不公开，因此只能由管理员进行注册
class IsPulicAuthorizedUnregisteredOrAdminOrDeny(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        contest = Contest.objects.get(pk=view.kwargs['pk'])
        return (
            contest.public and
            request.user and
            is_authenticated(request.user) and
            not request.user.contest_account.filter(contest=contest)
        ) or (
            not contest.public and
            request.user.is_staff
        )
