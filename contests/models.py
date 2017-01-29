from django.db import models
from django.utils.timezone import now

from django.contrib.auth.models import User
from problems.models import Problem
from submissions.models import Submission


class Contest(models.Model):
    """基础信息"""
    # 编号
    id = models.AutoField('编号', primary_key=True)
    # 标题
    title = models.CharField('标题', max_length=100, blank=True)
    # 比赛类型
    public = models.BooleanField('开放', default=True)
    # 比赛是否正式发布
    published = models.BooleanField('发布', default=False)

    """时间数据"""
    # 开始时间
    start_time = models.DateTimeField('开始时间')
    # 结束时间
    end_time = models.DateTimeField('结束时间')
    # 创建时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    """相关信息"""
    # 公告
    announcement = models.TextField(
        '公告', max_length=500, blank=True, null=True
    )
    # 作者
    author = models.ForeignKey(
        User, models.SET_NULL, blank=True, null=True,
        related_name='created_contests',
    )

    # 比赛状态
    @property
    def status(self):
        current_time = now()
        if current_time < self.start_time:
            return 'Pending'
        if current_time < self.end_time:
            return 'Running'
        return 'Ended'

    class Meta:
        ordering = ['-id']
        verbose_name = verbose_name_plural = '比赛'

    def __str__(self):
        return 'Contest %d' % (self.id)


# Reference:
# https://docs.djangoproject.com/en/1.10/ref/models/fields/#django.db.models.SET
def get_sentinel_user():
    return Uesr.objects.get_or_create(username='deleted')[0]


# 比赛账号
class ContestAccount(models.Model):
    # 实际是哪个User 即用哪个User登录
    user = models.ForeignKey(
        User, models.SET(get_sentinel_user),
        related_name='contest_account'
    )
    # 属于哪个比赛
    contest = models.ForeignKey(
        Contest, models.CASCADE,
        related_name='participants'
    )
    # 比赛中显示的名称 即队伍名
    name = models.CharField('队伍名', max_length=100, blank=True)
    # 注册参加比赛的时间
    date_joined = models.DateTimeField('注册时间', auto_now_add=True)

    """排名信息"""
    accept_count = models.IntegerField('通过题数', default=0)
    submit_count = models.IntegerField('提交次数', default=0)
    penalty = models.IntegerField('罚时', default=0)

    class Meta:
        ordering = ('contest', 'date_joined', 'user')
        unique_together = ('user', 'contest')
        verbose_name = verbose_name_plural = '比赛账号'

    def __str__(self):
        return '%s, Team %s(%s)' % (
            self.contest,
            self.name,
            self.user.username
        )


# 比赛题目
class ContestProblem(models.Model):
    # 比赛中的题目顺序编号
    sort = models.IntegerField()
    # 属于哪个比赛
    contest = models.ForeignKey(
        Contest, models.CASCADE,
        related_name='problems'
    )
    # 实际是哪个题目
    problem = models.ForeignKey(
        Problem, models.SET_NULL, null=True,
        related_name='involved_contests',
    )

    class Meta:
        ordering = ('contest', 'sort')
        unique_together = ('contest', 'sort')
        verbose_name = verbose_name_plural = '比赛题目'

    def __str__(self):
        return '%s, Problem %d(%d)' % (
            self.contest,
            self.sort,
            self.problem.id,
        )


# 比赛提交
class ContestSubmission(models.Model):
    # 比赛中的题目
    problem = models.ForeignKey(
        ContestProblem, models.CASCADE,
        related_name='submissions'
    )
    # 实际是哪个Submission
    submission = models.OneToOneField(
        Submission, models.CASCADE,
        related_name='involved_contest'
    )

    class Meta:
        unique_together = ('problem', 'submission')
        ordering = ('submission', 'problem')
        verbose_name = verbose_name_plural = '比赛提交'

    def __str__(self):
        return '%s, Submission %d' % (
            self.problem,
            self.submission.id
        )


# 比赛数据 即每个比赛每道题每个比赛账号的数据
class ContestStatistic(models.Model):
    # 属于哪个比赛
    contest = models.ForeignKey(
        Contest, models.CASCADE,
        related_name='statistic'
    )
    # 属于哪个参赛账号
    account = models.ForeignKey(
        ContestAccount, models.SET(get_sentinel_user),
        related_name='statistic'
    )
    # 哪道题
    problem = models.ForeignKey(
        ContestProblem, models.CASCADE,
        related_name='statistic'
    )
    # 通过/提交次数 -> $wa = $submit - $ac
    accept_count = models.IntegerField(default=0)
    submit_count = models.IntegerField(default=0)
    # 首次通过时间(s)
    accept_time = models.IntegerField(default=0)

    class Meta:
        unique_together = ('contest', 'account', 'problem')
        verbose_name = verbose_name_plural = '比赛数据'

    def __str__(self):
        return '%s, %s' % (self.account, self.problem)
