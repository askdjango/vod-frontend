from django.http import JsonResponse
from django.shortcuts import render
from .utils import get_comic_info


def index(request):
    return render(request, 'mychart/index.html')


def data_json(request):
    comic = get_comic_info(20853, '마음의 소리')
    return JsonResponse({
        'labels': [ep['title'] for ep in comic['ep_list']],
        'datasets': [{
            'label': '평점',
            'backgroundColor': 'rgba(255, 99, 132, 0.5)',
            'borderColor': 'rgba(255, 99, 132, 1)',
            'pointBackgroundColor': 'rgba(255, 99, 132, 1)',
            'pointBorderColor': '#fff',
            'data': [ep['rating'] for ep in comic['ep_list']],
        }],
    })

