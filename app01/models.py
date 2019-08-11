from django.db import models
from DjangoUeditor.models import UEditorField


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名称')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='文章标题')
    # category = models.CharField(max_length=50, blank=True, verbose_name='文章标签')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField(auto_now_add=True, editable=True, verbose_name='发布时间')
    update_time = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    # content = models.TextField(blank=True, null=True, verbose_name='文章内容')
    content = UEditorField(height=300, width=1000, default='', blank=True, imagePath='uploads/blog/images/',
                           toolbars='besttome', filePath='uploads/blog/files', verbose_name='文章内容')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = '文章'
        verbose_name_plural = '文章'
