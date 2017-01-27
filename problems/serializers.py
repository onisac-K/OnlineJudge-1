from rest_framework import serializers

from problems.models import Problem

# 题目列表
class ProblemListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Problem
        fields = ('id', 'title', 'url', 'source',
                  'accept_count', 'submit_count')


# 题目细节
class ProblemDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    author_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        lookup_field='username',
        view_name='user-detail',
        source='author'
    )

    class Meta:
        model = Problem
        exclude = ('description_md', 'input_description_md',
                   'output_description_md', 'hint_md', 'reserved')


# 修改题目
class ProblemUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        exclude = ('description', 'input_description', 'output_description',
                   'hint', 'author', 'accept_count', 'submit_count', 'create_time')


# 题目细节-管理员
class AdminProblemDetailSerializer(ProblemDetailSerializer):

    class Meta:
        model = Problem
        fields = '__all__'


# 题目细节-简单-即比赛状态
class BriefProblemDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        exclude = ('description_md', 'input_description_md',
                   'output_description_md', 'hint_md', 'reserved',
                   'author', 'id')
