from rest_framework import viewsets

from submissions.models import Submission
from submissions.serializers import SubmissionSerializer, SubmissionDetailSerializer


class SubmissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

    # 根据执行动作，细分使用的序列化对象
    # TODO: 找更好的方法
    def get_serializer_class(self):
        if not hasattr(self, 'action') or self.action == 'list':
            return SubmissionSerializer
        elif self.action == 'retrieve':
            return SubmissionDetailSerializer
        else:
            raise Exception('%s' % self.action)
