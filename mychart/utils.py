import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_comic_info(comic_id, comic_title):
    ep_list = []
    for page in range(1, 6): # 최대 5페이지
        params = {
            'titleId': comic_id,
            'page': page,
        }
        resp = requests.get('http://comic.naver.com/webtoon/list.nhn', params=params)
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        for tr in soup.select('#content table tr'):
            try:
                link = tr.select('.title a[href*=detail]')[0]
                rating = tr.select('.rating_type strong')[0].text
                date = tr.select('.num')[0].text
            except IndexError:
                continue

            title = link.text
            url = urljoin(resp.request.url, link['href'])

            ep = {
                'title': title,
                'url': url,
                'rating': rating,
                'date': date,
            }

            if ep in ep_list:
                return ep_list

            ep_list.append(ep)

    return {
        'title': comic_title,
        'ep_list': ep_list,
    }

