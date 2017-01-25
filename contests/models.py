from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from problems.models import Problem


class Contest(models.Model):
    """基础信息"""
    # 编号
    id = models.AutoField('编号', primary_key=True)
    # 标题
    title = models.CharField('标题', max_length=100, blank=True)
    # 比赛类型
    public = models.BooleanField('开放', default=True)
    # 私有比赛时，允许参加的账号
    participants = models.ManyToManyField(User, related_name='joined_contests')
    # # 比赛题目
    # problems = models.ManyToManyField(Problem, related_name='contests')
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
        User, blank=True, null=True, related_name='created_contests',
        on_delete=models.SET_NULL
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
        ordering = ['id']
        verbose_name = '比赛'
        verbose_name_plural = '比赛'

    def __str__(self):
        return '[%d] %s' % (self.id, self.title)


class ContestProblem(models.Model):
    # 比赛中的题目顺序编号
    sort = models.IntegerField()
    # 属于哪个比赛
    contest = models.ForeignKey(
        Contest,
        related_name='problems',
        on_delete=models.CASCADE
    )
    # 实际是哪个题目
    problem = models.ForeignKey(
        Problem,
        null=True,
        related_name='contests',
        on_delete=models.SET_NULL
    )

    class Meta:
        unique_together = ('contest', 'sort')
        ordering = ('contest', 'sort')
        verbose_name = '比赛题目'
        verbose_name_plural = '比赛题目'

    def __str__(self):
        return 'Contest %d. %s, Problem %d. %s' % (self.contest.id, self.contest.title, self.problem.id, self.problem.title)

