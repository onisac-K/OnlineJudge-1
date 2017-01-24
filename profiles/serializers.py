from rest_framework import serializers

from profiles.models import Profile
from django.contrib.auth.models import User


# 用户注册
class UserSignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


# 用户信息
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'profile')
        depth = 1


# 排行榜
class RanklistSerializer(serializers.HyperlinkedModelSerializer):
    # 指向用户详细资料的URL
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        lookup_field='username',
        view_name='user-detail'
    )

    # 排行榜需要用到的用户资料
    nickname = serializers.ReadOnlyField(source='profile.nickname')
    motto = serializers.ReadOnlyField(source='profile.motto')
    accept = serializers.ReadOnlyField(source='profile.accept_count')
    submit = serializers.ReadOnlyField(source='profile.submit_count')

    class Meta:
        model = User
        fields = ('url', 'username', 'nickname', 'motto', 'accept', 'submit')
