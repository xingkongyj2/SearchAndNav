from SearchAndNavAPP.models import searchClass
from SearchAndNavAPP.models import searchSite

def getData():
    all_data ={}

    search_class = searchClass.objects.values('name')
    searchs_ite = searchSite.objects.values()
    for i in search_class:
        all_data[i['name']]=[]

    for i in searchs_ite:  # 根据一级分类分类
        all_data[i['site_class_id']].append(i)
    return search_class,all_data,