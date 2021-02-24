from django.shortcuts import render
from django.http import HttpResponse
from SearchAndNavAPP.views import searchData
from SearchAndNavAPP.views import navData
from django.shortcuts import render
from SearchAndNavAPP.models import cardFirstClass
from SearchAndNavAPP.models import cardSecondeClass
from SearchAndNavAPP.models import card
from SearchAndNavAPP.views import suggest


#主函数只写最外层函数，接受其他文件整合好的数据，传入前端
def search(request):
    search_class=searchData.getData()[0]
    search_data=searchData.getData()[1]
    return render(request, 'SearchAndNavAPP/search.html',{'search_class':search_class,'search_data':search_data})

def search_simple(request):
    search_class=searchData.getData()[0]
    search_data=searchData.getData()[1]
    return render(request, 'SearchAndNavAPP/search_simple.html',{'search_class':search_class,'search_data':search_data})

#导航
def nav(request):
    tmp=navData.getData()
    navdatas=tmp[0]
    FirstClass=tmp[1]
    back=tmp[2]
    return render(request, 'SearchAndNavAPP/nav.html',{'navdatas': navdatas,'FirstClass':FirstClass,'back':back})

def get_click_number(request):
    card_id=request.GET.get('card_id')
    card_item=card.objects.get(id=card_id)#获取到一条数据
    card_item.click=card_item.click+1#获取数据并且加一
    card_item.save()#别忘了保存
    return HttpResponse()

def get_click_awesome(request):
    card_id=request.GET.get('card_id')
    card_item=card.objects.get(id=card_id)#获取到一条数据
    card_item.awesome=card_item.awesome+1#获取数据并且加一
    card_item.save()#别忘了保存
    return HttpResponse(card_item.awesome)
    return render(request, 'SearchAndNavAPP/nav.html', {'navdatas': navdatas, 'FirstClass': FirstClass, 'back': back})


def get_suggest_search(request):
    key = request.GET.get('key')
    search_data = suggest.getSearch(key)
    return render(request, 'SearchAndNavAPP/search_suggest.html', {'search_data': search_data})


def get_suggest_movie(request):
    key = request.GET.get('key')
    movie_data=suggest.getMovie(key)
    return render(request, 'SearchAndNavAPP/movie.html',{'movie_data':movie_data})



def get_suggest_book(request):
    key = request.GET.get('key')
    book_data = suggest.getBook(key)
    return render(request, 'SearchAndNavAPP/book.html', {'book_data': book_data})

