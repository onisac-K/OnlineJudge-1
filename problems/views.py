from rest_framework import viewsets
from rest_framework import generics
from rest_framework import renderers
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from problems.models import Problem
from problems import permissions, utils
from problems.serializers import ProblemListSerializer, ProblemDetailSerializer, ProblemUpdateSerializer

from submissions.models import Submission
from submissions.serializers import NewSubmissionSerializer, SubmissionSerializer

from pprint import pprint


# 题目列表
class ProblemListAPIView(generics.ListAPIView):

    queryset = Problem.objects.all()
    serializer_class = ProblemListSerializer


# 题目细节
class ProblemDetailAPIView(generics.RetrieveAPIView):

    queryset = Problem.objects.all()
    serializer_class = ProblemDetailSerializer


# 题目提交
# GET  - 当前用户提交列表
# POST - 当前用户创建提交（最近5次）
class ProblemSubmitAPIView(generics.ListCreateAPIView):
    
    def get_queryset(self):
        problem = self.kwargs['pk']
        return Submission.objects.filter(author=self.request.user, problem__id=problem)[:5]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubmissionSerializer
        elif self.request.method == 'POST':
            return NewSubmissionSerializer

    def perform_create(self, serializer):
        problem = Problem.objects.get(pk=self.kwargs['pk'])
        serializer.save(author=self.request.user, problem=problem)
