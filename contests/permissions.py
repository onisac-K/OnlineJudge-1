from rest_framework import permissions


# 比赛提交 - 只允许作者或管理员访问提交细节
class IsAuthorOrAdminOrDeny(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.submission.author == request.user or request.user.is_staff
