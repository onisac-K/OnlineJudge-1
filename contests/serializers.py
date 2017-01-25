from rest_framework import serializers
from rest_framework.reverse import reverse

from contests.models import Contest, ContestProblem
from utils.serializers import MultiParamsHyperlinkedIdentityField


# 比赛列表
class ContestListSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        lookup_field='username',
        view_name='user-detail'
    )

    class Meta:
        model = Contest
        fields = ('id', 'url', 'title', 'public',
                  'start_time', 'end_time', 'status', 'author')


# 比赛题目
class ContestProblemSerializer(serializers.ModelSerializer):

    url = MultiParamsHyperlinkedIdentityField(
        lookup_fields=(('contest__id', 'contest_id'),
                       ('sort', 'problem_sort')),
        view_name='contestproblem-detail',
        read_only=True
    )

    class Meta:
        model = ContestProblem
        fields = ('sort', 'problem', 'url')


# 比赛题目细节
class ContestProblemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContestProblem
        fields = '__all__'
        depth = 1


# 比赛细节
class ContestDetailSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        lookup_field='username',
        view_name='user-detail'
    )

    problems = ContestProblemSerializer(many=True, read_only=True)

    class Meta:
        model = Contest
        fields = ('id', 'title', 'public', 'problems', 'start_time',
                  'end_time', 'announcement', 'author', 'status')


# # 比赛题目列表
# class ContestProblemListSerializer(serializers.ModelSerializer):

#     sort = serializers.HyperlinkedRelatedField(
#         read_only=True,
#         lookup_field='pk',
#         view_name='contest-problem'
#     )

#     class Meta:
#         model = ContestProblem
#         fields = '__all__'
