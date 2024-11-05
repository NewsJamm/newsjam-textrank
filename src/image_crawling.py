import requests
from bs4 import BeautifulSoup


def fetch_main_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTP 오류 발생 시 예외를 발생시킴
        soup = BeautifulSoup(response.text, 'html.parser')

        # Open Graph 태그에서 대표 이미지 찾기
        og_image = soup.find('meta', property='og:image')
        if og_image and og_image['content']:
            return og_image['content']

        # og:image가 없는 경우, 첫 번째 img 태그 사용
        img_tag = soup.find('img')
        if img_tag and img_tag.get('src'):
            return img_tag['src']

    except Exception as e:
        print(f"Error occurred: {e}")  # 에러 메시지 출력 (선택 사항)

    return None