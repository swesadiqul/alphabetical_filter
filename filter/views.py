from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import *

# Create your views here.
def index(request):
    letestnews = LetestNews.objects.all()

    context = {'letestnews': letestnews}
    return render(request, 'index.html', context)

def filter_data(request):
    receive_char = request.GET.get('key')

    news_filter = LetestNews.objects.all()
    if receive_char != "All":
        news_filter = LetestNews.objects.filter(title__startswith=receive_char)
    else:
        news_filter = LetestNews.objects.all()

    temp = render_to_string('news/news_filter.html', {'news_filter': news_filter})
    return JsonResponse({'data':temp})