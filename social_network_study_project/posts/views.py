from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    #запрос к БД сортировка по убыванию и вывод первых 10
    latest = Post.objects.order_by('-pub_date')[:10]
    #собираем тексты постов в один, разделяя новой строкой
    output=[]
    for item in latest:
        output.append(item.text)
    return HttpResponse('\n'.join(output))
