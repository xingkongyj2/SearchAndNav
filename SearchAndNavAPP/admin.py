from django.contrib import admin
from django import forms
from .models import cardFirstClass
from .models import cardSecondeClass
from .models import card
from .models import searchClass
from .models import searchSite







class showSearchClass(admin.ModelAdmin):  # 配置类 选择要展示的字段
    list_display = ('id', 'name', 'priority', 'created')  # list_display支持list tuple
    list_editable = ['priority']
    list_display_links = ('name',)
admin.site.register(searchClass, showSearchClass)


class showsearchSite(admin.ModelAdmin):  # 配置类 选择要展示的字段
    list_display = ('id', 'name', 'priority', 'created','logo','site_class')  # list_display支持list tuple
    list_editable = ['priority','site_class']
    list_display_links = ('name',)
    list_filter = ('site_class', 'priority')  # 过滤器
    search_fields = ('name',)  # 搜索字段
admin.site.register(searchSite, showsearchSite)



class showCardFirstClass(admin.ModelAdmin):  # 配置类 选择要展示的字段
    list_display=('id', 'name', 'priority','created')   #list_display支持list tuple
    list_editable = ['priority']
    list_display_links = ('name',)
admin.site.register(cardFirstClass,showCardFirstClass)


class showCardSecondeClass(admin.ModelAdmin):  # 配置类 选择要展示的字段
    list_display=('id', 'name', 'priority','class_name','background_data','created')   #list_display支持list tuple
    list_editable = ['priority','class_name']
    list_display_links = ('name',)
    list_filter = ('class_name','priority')  # 过滤器
    search_fields = ('background','name')  # 搜索字段
admin.site.register(cardSecondeClass,showCardSecondeClass)



class showCard(admin.ModelAdmin):  # 配置类 选择要展示的字段
    list_display=('id', 'name', 'priority','url_data','description','image_data','lable','awesome','click','card_class_first','card_class_second','created')   #list_display支持list tuple
    # list_editable 设置默认可编辑字段，直接在列表中编辑。不建议
    list_editable = ['priority','card_class_first','card_class_second','lable']
    # list_per_page设置每页显示多少条记录，默认是100条
    #list_per_page = 50
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('name',)
    # 筛选器
    list_filter = ('card_class_first','card_class_second','priority')  # 过滤器
    search_fields = ('name',)  # 搜索字段
admin.site.register(card,showCard)


admin.site.site_header = 'All for one后台'
admin.site.site_title = 'All for one'

