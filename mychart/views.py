from django.http import JsonResponse
from django.shortcuts import render
from chartjs.views.lines import BaseLineChartView
from .utils import get_comic_info


def index(request):
    return render(request, 'mychart/index.html')


class WebtoonChartJSONView(BaseLineChartView):
    def __init__(self):
        super().__init__()
        self.comic = get_comic_info(20853, '마음의 소리')

    def get_labels(self):
        return [ep['title'] for ep in self.comic['ep_list']]

    def get_providers(self):
        return ['평점']

    def get_data(self):
        return [
            [ep['rating'] for ep in self.comic['ep_list']],
        ]

    def get_colors(self):
        yield (255, 99, 132)

data_json = WebtoonChartJSONView.as_view()

