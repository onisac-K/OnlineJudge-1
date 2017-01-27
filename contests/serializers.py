from rest_framework import serializers
from rest_framework.reverse import reverse

from contests.models import (
    Contest,
    ContestAccount,
    ContestProblem,
    ContestSubmission,
    ContestStatistic,
)
from utils.serializers import MultiParamsHyperlinkedIdentityField

from problems.serializers import BriefProblemDetailSerializer

from submissions.serializers import BriefSubmissionSerializer


# 比赛列表
class ContestListSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField()
    author_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        lookup_field='username',
        view_name='user-detail',
        source='author'
    )

    class Meta:
        model = Contest
        fields = ('id', 'url', 'title', 'public', 'status',
                  'start_time', 'end_time', 'author_url', 'author')


# 比赛题目列表
# 只是比赛题目 将被包含在{{比赛细节}}中
class ContestProblemSerializer(serializers.ModelSerializer):

    url = MultiParamsHyperlinkedIdentityField(
        lookup_fields=(('contest__id', 'contest_id'),
                       ('sort', 'problem_sort')),
        view_name='contest-problem-detail',
        read_only=True
    )

    class Meta:
        model = ContestProblem
        fields = ('sort', 'problem', 'url')


# 比赛细节
class ContestDetailSerializer(serializers.ModelSerializer):
    problems = ContestProblemSerializer(many=True, read_only=True)

    class Meta:
        model = Contest
        fields = ('id', 'title', 'problems', 'start_time',
                  'end_time', 'announcement', 'status')


# 比赛题目细节
class ContestProblemDetailSerializer(serializers.ModelSerializer):
    problem = BriefProblemDetailSerializer(read_only=True)

    class Meta:
        model = ContestProblem
        fields = ('sort', 'problem')


# 比赛提交列表
class ContestSubmissionListSerializer(serializers.ModelSerializer):
    submission = BriefSubmissionSerializer(read_only=True)
    problem = serializers.SlugRelatedField(read_only=True, slug_field='sort')

    class Meta:
        model = ContestSubmission
        fields = ('problem', 'submission',)
