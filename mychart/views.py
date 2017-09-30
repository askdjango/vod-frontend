from django.shortcuts import render
from .utils import get_comic_info


def index(request):
    comic = get_comic_info(20853, '마음의 소리')
    return render(request, 'mychart/index.html', {
        'comic': comic,
    })

