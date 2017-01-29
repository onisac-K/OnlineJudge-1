from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

from contests.models import (
    Contest,
    ContestAccount,
    ContestProblem,
    ContestSubmission,
    ContestStatistic,
)

from contests.serializers import (
    ContestListSerializer,
    ContestDetailSerializer,
    ContestProblemDetailSerializer,
    ContestSubmissionListSerializer,
    ContestSubmissionDetailSerializer,
    ContestParticipantListSerializer,
    NewContestAccountSerializer,
)

from submissions.models import Submission
from submissions.serializers import NewSubmissionSerializer

from contests.permissions import (
    IsParticipantOrAdminOrDeny,
    IsAuthorOrAdminOrDeny,
    IsPulicAuthorizedUnregisteredOrAdminOrDeny
)


# 比赛列表
class ContestListAPIView(generics.ListAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestListSerializer


# 比赛细节
class ContestDetailAPIView(generics.RetrieveAPIView):
    queryset = Contest.objects.all()
    permission_classes = [IsAuthenticated,
                          IsParticipantOrAdminOrDeny,]
    serializer_class = ContestDetailSerializer


# 比赛题目细节
class ContestProblemDetailAPIView(generics.RetrieveAPIView):
    queryset = ContestProblem.objects.all()
    serializer_class = ContestProblemDetailSerializer
    lookup_fields = (
        ('contest__id', 'contest_id'),
        ('sort', 'problem_sort')
    )

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {x[0]: self.kwargs[x[1]] for x in self.lookup_fields}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj


# 比赛提交状态(列表 全部)
class ContestSubmissionListAPIView(generics.ListAPIView):
    queryset = ContestSubmission.objects.all()
    serializer_class = ContestSubmissionListSerializer


# 比赛提交状态(细节)
class ContestSubmissionDetailAPIView(generics.RetrieveAPIView):
    queryset = ContestSubmission.objects.all()
    serializer_class = ContestSubmissionDetailSerializer
    permission_classes = [IsAuthorOrAdminOrDeny, ]
    lookup_fields = (
        ('problem__contest__id', 'contest_id'),
        ('submission__id', 'submission_id')
    )

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {x[0]: self.kwargs[x[1]] for x in self.lookup_fields}
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj


# 比赛提交状态
class ContestProblemSubmissionListAPIView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        if self.request.method == 'GET':
            cid, pid = self.kwargs['contest_id'], self.kwargs['problem_sort']
            submissions = ContestSubmission.objects.filter(
                submission__author=self.request.user,
                problem__contest__id=cid
            )
            return pid and submissions.filter(problem__sort=pid) or submissions

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContestSubmissionListSerializer
        elif self.request.method == 'POST':
            return NewSubmissionSerializer

    def perform_create(self, serializer):
        contest_problem = ContestProblem.objects.get(
            contest__id=self.kwargs['contest_id'],
            sort=self.kwargs['problem_sort']
        )
        submission = serializer.save(
            author=self.request.user,
            problem=contest_problem.problem
        )
        ContestSubmission.objects.create(
            problem=contest_problem,
            submission=submission
        )


# 比赛参赛人员
class ContestParticipantListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsPulicAuthorizedUnregisteredOrAdminOrDeny, ]

    def get_queryset(self):
        cid = self.kwargs['pk']
        return ContestAccount.objects.filter(contest__id=cid)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContestParticipantListSerializer
        elif self.request.method == 'POST':
            return NewContestAccountSerializer

    def perform_create(self, serializer):
        contest = Contest.objects.get(pk=self.kwargs['pk'])
        serializer.save(
            contest=contest,
            user=self.request.user
        )
