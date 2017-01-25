from django.db import models
from django.contrib.auth.models import User
from utils.models import CodeLang

from markdown import markdown


class Problem(models.Model):
    """基本信息"""
    # 编号
    id = models.AutoField('编号', primary_key=True)
    # 标题
    title = models.CharField('标题', max_length=100, blank=True)
    # 作者
    author = models.ForeignKey(
        User, blank=True, null=True, related_name='problems',
        on_delete=models.SET_NULL
    )
    # 允许的语言
    languages = models.ManyToManyField(CodeLang, related_name='languages')

    """描述信息"""
    # 题目/输入/输出描述
    description = models.TextField('题目描述 [HTML]', blank=True)
    description_md = models.TextField('题目描述 [Markdown]', blank=True)
    input_description = models.TextField('输入描述 [HTML]', blank=True)
    input_description_md = models.TextField('输入描述 [Markdown]', blank=True)
    output_description = models.TextField('输出描述 [HTML]', blank=True)
    output_description_md = models.TextField('输出描述 [Markdown]', blank=True)
    # 样例输入/输出
    sample_input = models.TextField('样例输入', blank=True)
    sample_output = models.TextField('样例输出', blank=True)
    # 来源
    source = models.CharField('来源', max_length=50, blank=True)
    # 提示
    hint = models.TextField('提示 [HTML]', blank=True)
    hint_md = models.TextField('提示 [Markdown]', blank=True)

    """数据信息"""
    # 创建时间
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    # 时间/内存限制
    time_limit = models.IntegerField('时间限制(ms)', default=1000)
    memory_limit = models.IntegerField('内存限制(MB)', default=128)
    # 通过/提交数量
    accept_count = models.IntegerField('通过数量', default=0)
    submit_count = models.IntegerField('提交数量', default=0)
    # 题目是否保留
    reserved = models.BooleanField('题目不可见', default=True)

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = '题目'
        ordering = ('id',)

    # 解析Markdown，然后再保存其它字段
    # TODO: 代码段高亮，转义，但是文本段支持内嵌html
    # TODO: MathJax
    def save(self, *args, **kwargs):
        self.description = markdown(self.description_md, safe_mode='escape')
        self.input_description = markdown(self.input_description_md)
        self.output_description = markdown(self.output_description_md)
        self.hint = markdown(self.hint_md)
        super(Problem, self).save(*args, **kwargs)

    def __str__(self):
        return '[%d] %s' % (self.id, self.title)
