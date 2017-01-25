from django.db import models


class CodeLang(models.Model):
    # 编号
    id = models.AutoField('编号', primary_key=True)
    # 语言名称
    name = models.CharField('语言名称', max_length=10, blank=True)

    class Meta:
        verbose_name = '编程语言'
        verbose_name_plural = '编程语言'

    def __str__(self):
        return self.name
