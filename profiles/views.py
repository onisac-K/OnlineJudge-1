from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from django.contrib.auth.models import User
from profiles.serializers import RanklistSerializer, UserProfileSerializer, UserSignUpSerializer


# 排行榜
class RanklistAPIView(generics.ListAPIView):
    queryset = User.objects.order_by(
        '-profile__accept_count',
        'profile__submit_count'
    )
    serializer_class = RanklistSerializer
    # renderer_classes = (TemplateHTMLRenderer,)
    # template_name = './profiles/ranklist.html'

# 用户信息
class UserProfileAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'username'
    # renderer_classes = (TemplateHTMLRenderer,)
    # template_name = './profiles/profile.html'


# 注册
class SignUpAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

    def get(self, request, format=None):
        return Response({'info': '注册页面'})

    def perform_create(self, serializer):
        User.objects.create_user(**serializer.validated_data)
