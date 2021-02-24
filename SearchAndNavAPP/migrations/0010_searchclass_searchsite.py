# Generated by Django 3.0.7 on 2020-06-24 05:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SearchAndNavAPP', '0009_card_lable'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchClass',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='类名')),
                ('priority', models.IntegerField(default=1, verbose_name='优先级')),
            ],
            options={
                'verbose_name': '搜索类型',
                'verbose_name_plural': '搜索类型',
                'ordering': ('-priority', 'created'),
            },
        ),
        migrations.CreateModel(
            name='searchSite',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='时间')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='网站名')),
                ('priority', models.IntegerField(default=1, verbose_name='优先级')),
                ('url', models.TextField(verbose_name='网址')),
                ('logo', models.TextField()),
                ('site_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SearchAndNavAPP.searchClass', to_field='name', verbose_name='网站分类')),
            ],
            options={
                'verbose_name': '聚合搜索网站',
                'verbose_name_plural': '聚合搜索网站',
                'ordering': ('-priority', 'created'),
            },
        ),
    ]
