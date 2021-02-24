from SearchAndNavAPP.models import cardFirstClass
from SearchAndNavAPP.models import cardSecondeClass
from SearchAndNavAPP.models import card

def getData():
    all_data=[]#获取数据以列表形式
    all_data2 = {}#获取数据以列表字典形式，需要传到前端
    firstClass=[]#把一级类分类
    back={}#二级菜单背景颜色
    SecondeClassPriority={}#建立二级菜单的优先级字典，方便查询

    FirstClass=cardFirstClass.objects.values_list('name')#用列表获取
    SecondeClass=cardSecondeClass.objects.values('name','priority','background')#查询到的是QuerySet类型，实际是一个列表.每条信息是字典
    Card = card.objects.values() # 获取全部字段
    #让二级类和它的背景形成键值对
    for tmp in SecondeClass:
        back[tmp["name"]]=tmp['background']
        SecondeClassPriority[tmp["name"]]=tmp['priority']

    FirstClassdatas = {}
    for i in FirstClass:#先根据一级列表建立空的列表
        if i[0]!="null":
            FirstClassdatas[i[0]] = []
            firstClass.append(i[0])
    for i in Card:#根据一级分类去二级分类
        FirstClassdatas[i['card_class_first_id']].append(i)

    for FirstClassdata in FirstClassdatas.values():#一级分类后是一个列表FirstClassdata，每一项是一个字典
        SecondeClassdatas = {}#二级分类
        SecondeClassdatas2 = {}  # 二级分类
        for item in FirstClassdata:#遍历一级分类，创看看这个一级分类下都有那些二级菜单。并把二级菜单填上他们的优先级
            SecondeClassdatas2[item['card_class_second_id']]=SecondeClassPriority[item['card_class_second_id']]
        SecondeClassdatas2=sorted(SecondeClassdatas2.items(), key=lambda x: x[1], reverse=True)#用优先级进行排序
        for item in SecondeClassdatas2:
            SecondeClassdatas[item[0]]=[]#得到正确的二级优先级列表

        for item in FirstClassdata:#
            SecondeClassdatas[item['card_class_second_id']].append(item)
        #使用直接SecondeClassdatas传到前端去打印.前端打印格式如下
        all_data.append(SecondeClassdatas)

    for i in range(len(firstClass)):
        all_data2[firstClass[i]]=all_data[i]
    return all_data2,firstClass,back,
