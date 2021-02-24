from django import template
 
register = template.Library()
 


#定义了background函数，并且注册
@register.filter(name='background')
def background(dictionary, key):
    return dictionary.get(key)