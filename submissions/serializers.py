from rest_framework import serializers

from utils.serializers import MultiParamsHyperlinkedIdentityField

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
    status = serializers.SerializerMethodField()

    class Meta:
        model = Submission
        fields = ('id', 'author', 'problem', 'submit_time',
                  'status', 'language', 'url', 'author_url')

    def get_status(self, obj):
        return obj.get_status_display()


# 提交列表 - 简略 即比赛时显示的列表
# TODO: url改为比赛内的url
class BriefSubmissionSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()
    status = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Submission
        fields = ('id', 'submit_time', 'status', 'notes',
                  'language', 'exec_memory', 'exec_time', 'author')

    def get_status(self, obj):
        return obj.get_status_display()


# 提交细节
class SubmissionDetailSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    language = serializers.StringRelatedField()

    class Meta:
        model = Submission
        exclude = ('author', 'source_code')

    def get_status(self, obj):
        return obj.get_status_display()


# 增加提交
class NewSubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = ('source_code', 'language')


# 增加提交 - 带题号
class NewSubissionWithPIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = ('problem', 'language', 'source_code')
