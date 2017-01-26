from rest_framework import serializers

from submissions.models import Submission


class SubmissionSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.HyperlinkedRelatedField(
        read_only=True,
        lookup_field='username',
        view_name='user-detail'
    )

    language = serializers.StringRelatedField()

    class Meta:
        model = Submission
        fields = ('id', 'author', 'problem', 'source_code',
                  'submit_time', 'status', 'language','url')


class SubmissionDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = '__all__'
