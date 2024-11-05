import requests
from bs4 import BeautifulSoup


def fetch_main_image(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Open Graph 태그에서 대표 이미지 찾기
    og_image = soup.find('meta', property='og:image')
    if og_image and og_image['content']:
        return og_image['content']

    # og:image가 없는 경우, 첫 번째 img 태그 사용
    img_tag = soup.find('img')
    if img_tag and img_tag.get('src'):
        return img_tag['src']

    return None