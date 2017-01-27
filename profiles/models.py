from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    # 账户 [username, email, password, last_login, date_joined]
    account = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )

    # 资料
    nickname = models.CharField('昵称', max_length=30, blank=True)
    realname = models.CharField('姓名', max_length=30, blank=True)
    student_id = models.CharField('学号', max_length=30, blank=True, null=True)
    blog = models.URLField('博客', blank=True, null=True)
    motto = models.CharField('签名', max_length=254, blank=True)

    # 刷题信息
    accept_problem_count = models.IntegerField('通过题目数', default=0)
    accept_count = models.IntegerField('通过提交次数', default=0)
    submit_count = models.IntegerField('提交次数', default=0)

    class Meta:
        ordering = ('account',)

    def __str__(self):
        return str(self.account)


# 创建profile
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile()
        profile.account = instance
        profile.save()

# 这一句使得创建User对象时，也创建一个profile对象
post_save.connect(create_user_profile, sender=User)
