from rest_framework import viewsets
from rest_framework import generics
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from problems.models import Problem
from problems import permissions
from problems.serializers import ProblemListSerializer, ProblemDetailSerializer, ProblemUpdateSerializer


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemListSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        permissions.IsAuthorOrAdminOrReadOnly,
        permissions.IsAuthorOrReservedProblemInvisable,
    )

    # 列举非保留的问题
    # TODO: filter
    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset
        return self.queryset.filter(reserved=False)

    # 根据执行动作，细分使用的序列化对象
    # TODO: 找更好的方法
    def get_serializer_class(self):
        if not hasattr(self, 'action') or self.action == 'list':
            return ProblemListSerializer
        elif self.action == 'retrieve':
            return ProblemDetailSerializer
        elif self.action in ['update', 'create', 'partial_update']:
            return ProblemUpdateSerializer
        else:
            raise Exception('%s' % self.action)

    # 创建题目时，当前用户作为作者
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
