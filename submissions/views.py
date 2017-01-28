from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import renderer_classes
from rest_framework.response import Response

from submissions.models import Submission
from submissions.serializers import SubmissionSerializer, SubmissionDetailSerializer
from submissions.permissions import IsAuthorOrAdminOrDeny

# 比赛外的提交情况
class SubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    # 限制在比赛外不可能访问到比赛内的Submission
    queryset = Submission.objects.filter(involved_contest=None)
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthorOrAdminOrDeny, ]

    # 根据执行动作，细分使用的序列化对象
    # TODO: 找更好的方法
    def get_serializer_class(self):
        if not hasattr(self, 'action') or self.action == 'list':
            return SubmissionSerializer
        elif self.action == 'retrieve':
            return SubmissionDetailSerializer
        else:
            raise Exception('%s' % self.action)
