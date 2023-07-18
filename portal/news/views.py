from django.shortcuts import render

from .models import News


def news_main(request):
    """Главная страница Новостей"""
    news_list = News.objects.all().order_by('-pub_date')
    context = {
        'news_list': news_list,
        }

    return render(request, 'news/news_main_page.html', context)


def news_detail(request, news_id):
    """Детализация Новости"""
    template = 'news/news_detail.html'
    news = News.objects.get(pk=news_id)
    context = {
        'news': news,
    }
    return render(request, template, context)