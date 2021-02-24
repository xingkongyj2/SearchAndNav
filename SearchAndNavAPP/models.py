from django.db import models

# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
from django.utils.html import format_html




class searchClass(models.Model):
    id=models.AutoField(primary_key=True)
    created = models.DateTimeField('时间',default=timezone.now)
    name = models.CharField('类名', max_length=100,unique=True)
    priority=models.IntegerField('优先级',default=1)
    class Meta:
        verbose_name = '搜索类型'
        verbose_name_plural='搜索类型'
        ordering = ('-priority','created')#先根据优先级排序再根据时间排序
    def __str__(self):
        return self.name

class searchSite(models.Model):
    id=models.AutoField(primary_key=True)
    created = models.DateTimeField('时间',default=timezone.now)
    name = models.CharField('网站名', max_length=100,unique=True)
    priority=models.IntegerField('优先级',default=1)
    url = models.TextField('网址')
    logo = models.TextField(default='null', null=True)
    site_class = models.ForeignKey(searchClass, to_field="name", verbose_name='网站分类', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '聚合搜索网站'
        verbose_name_plural='聚合搜索网站'
        ordering = ('-priority','created')#先根据优先级排序再根据时间排序
    def __str__(self):
        return self.name

















class cardFirstClass(models.Model):
    id=models.AutoField(primary_key=True)
    created = models.DateTimeField('时间',default=timezone.now)
    name = models.CharField('类名', max_length=100,unique=True)
    priority=models.IntegerField('优先级',default=1)

    class Meta:
        verbose_name = '卡片第一类型'
        verbose_name_plural='卡片第一类型'
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-priority','created')#先根据优先级排序再根据时间排序

    def __str__(self):
        # return self.title 将文章标题返回
        return self.name

class cardSecondeClass(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField('时间', default=timezone.now)
    name = models.CharField('类名', max_length=100,unique=True)
    priority = models.IntegerField('优先级', default=1)
    class_name= models.ForeignKey(cardFirstClass,to_field="name", verbose_name='一级分类', on_delete=models.CASCADE)
    background = models.CharField('背景',max_length=300)

    class Meta:
        verbose_name = '卡片第二类型'
        verbose_name_plural = '卡片第二类型'
        ordering = ('-priority','created')
    def __str__(self):
        # return self.title 将文章标题返回
        return self.name

    def background_data(self):  # 把logo的网址拿过来然后再加上html标签。在admin中就添加image_data字段
        return format_html(
            '<div style="{};width:40px;height:40px"></div>',
            self.background,
        )
    background_data.short_description = u'背景'


class card(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField('时间', default=timezone.now)
    name = models.CharField('网站名', max_length=100, unique=True)
    description = models.CharField('描述', max_length=100)
    priority = models.IntegerField('优先级', default=1)
    url= models.TextField('网址')
    logo=models.TextField()
    lable = models.CharField('标签',max_length=100, default="null")
    awesome = models.IntegerField('点赞',default=0)
    click = models.IntegerField('点击量',default=0)
    #外键关联后会自动有下拉框
    card_class_first = models.ForeignKey(cardFirstClass, to_field="name", verbose_name='一级分类', on_delete=models.CASCADE)
    card_class_second = models.ForeignKey(cardSecondeClass,to_field="name", verbose_name='二级分类', on_delete=models.CASCADE)
    class Meta:
        verbose_name = '卡片'
        verbose_name_plural = '卡片'
        ordering = ('-priority','created')
    def __str__(self):
        # return self.title 将文章标题返回
        return self.name

    def image_data(self):#把logo的网址拿过来然后再加上html标签。在admin中就添加image_data字段
        return format_html(
            '<img src="{}" width="32px"/>',
            self.logo,
        )
    image_data.short_description = u'图片'

    def image_data(self):#把logo的网址拿过来然后再加上html标签。在admin中就添加image_data字段
        return format_html(
            '<img src="{}" width="32px"/>',
            self.logo,
        )
    image_data.short_description = u'图片'


    def url_data(self):#把logo的网址拿过来然后再加上html标签。在admin中就添加image_data字段
        return format_html(
            '<a href="{}" target="_blank">{}</a>',
            self.url,self.url,
        )
    url_data.short_description = u'网址'





