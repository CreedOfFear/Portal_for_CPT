from django.shortcuts import render

from news.models import News


def index(request):
    news_list = News.objects.all().order_by('-pub_date')
    context = {
        'news_list': news_list
    }
    return render(request, 'main_page/main_page.html', context)
