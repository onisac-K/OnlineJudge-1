from rest_framework import generics
from rest_framework.response import Response

from django.contrib.auth.models import User
from profiles.serializers import RanklistSerializer, UserProfileSerializer, UserSignUpSerializer


# 排行榜
class RanklistAPIView(generics.ListAPIView):
    queryset = User.objects.order_by(
        '-profile__accept_count',
        'profile__submit_count'
    )
    serializer_class = RanklistSerializer


# 用户信息
class UserProfileAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'username'


# 注册
class SignUpAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

    def get(self, request, format=None):
        return Response({'info': '注册页面'})

    def perform_create(self, serializer):
        User.objects.create_user(**serializer.validated_data)
        