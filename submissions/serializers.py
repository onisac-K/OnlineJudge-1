from rest_framework import serializers

from submissions.models import Submission


# 提交列表
class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.StringRelatedField()
    author_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        lookup_field='username',
        view_name='user-detail',
        source='author'
    )
    language = serializers.StringRelatedField()

    class Meta:
        model = Submission
        fields = ('id', 'author', 'problem', 'submit_time',
                  'status', 'language', 'url', 'author_url')


# 提交细节
class SubmissionDetailSerializer(serializers.ModelSerializer):

    language = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    author_url = serializers.HyperlinkedRelatedField(
        read_only=True,
        lookup_field='username',
        view_name='user-detail',
        source='author'
    )

    class Meta:
        model = Submission
        fields = '__all__'


# 增加提交
class NewSubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = ('source_code', 'language')
