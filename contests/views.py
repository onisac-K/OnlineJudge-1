from rest_framework import generics
from rest_framework.response import Response

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
    # NewContestSubmissionSerializer
)

from submissions.models import Submission
from submissions.serializers import NewSubmissionSerializer


# 比赛列表
class ContestListAPIView(generics.ListAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestListSerializer


# 比赛细节
class ContestDetailAPIView(generics.RetrieveAPIView):
    queryset = Contest.objects.all()
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


# 比赛提交状态(全部)
class ContestStatusAPIView(generics.ListAPIView):
    queryset = ContestSubmission.objects.all()
    serializer_class = ContestSubmissionListSerializer


# 比赛提交列表(当前用户-全部) [GET:最近提交]
class ContestSubmissionListAPIView(generics.ListAPIView):

    def get_queryset(self):
        return ContestSubmission.objects.filter(problem__contest__id=self.kwargs['pk'])
        # problem_sort = self.kwargs['problem_sort']
        # if problem_sort == None:
        #     return ContestSubmission.objects.all()
        # else:
        #     return ContestSubmission.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContestSubmissionListSerializer
        # elif self.request.method == 'POST':
        #     return NewContestSubmissionSerializer
        else:
            raise Exception('Unhandled method: %s' % self.request.method)

    # def perform_create(self, serializer):
    #     print(self.kwargs)
    #     # problem_sort = self.kwargs['problem_sort']
    #     # contest_id = self.kwargs['contest_id']
    #     # contest_problem = ContestProblem.objects.get(contest__id=contest_id, sort=problem_sort)
    #     # problem = contest_problem.problem
    #     # serializer.save(author=self.request.user, problem=problem)


class ContestProblemSubmissionListAPIView(generics.ListCreateAPIView):

    def get_queryset(self):
        if self.request.method == 'GET':
            query = {
                'contest__id': self.kwargs['contest_id'],
                'sort': self.kwargs['problem_sort']
            }
            contest_problem = ContestProblem.objects.get(**query)
            query = {
                'problem': contest_problem,
                'submission__author': self.request.user
            }
            return ContestSubmission.objects.filter(**query)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContestSubmissionListSerializer
        elif self.request.method == 'POST':
            return NewSubmissionSerializer

    def perform_create(self, serializer):
        query = {
            'contest__id': self.kwargs['contest_id'],
            'sort': self.kwargs['problem_sort']
        }
        contest_problem = ContestProblem.objects.get(**query)
        problem = contest_problem.problem
        submission = serializer.save(author=self.request.user, problem=problem)
        ContestSubmission.objects.create(problem=contest_problem, submission=submission)
