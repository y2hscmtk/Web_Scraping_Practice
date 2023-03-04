import requests
from bs4 import BeautifulSoup


# 네이버 웹툰에 해당하는 url에 접속해서 BeautifulSoup 객체를 만듦
# 네이버 웹툰 스크래핑
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()  # 문제 발생시 종료

# html문서를 lxml를 통해서 BeautifulSoup객체로 만듦
soup = BeautifulSoup(res.text, "lxml")

# 조건에 해당하는 모든 element를 찾음
cartoons = soup.find_all(
    "a", attrs={"class": "ContentTitle__title_area--x24vt"})

for cartoon in cartoons:
    # ContentTitle__title_area--x24vt 클래스를 가진 a태그의 텍스트 정보를 가져옴 => 웹툰 제목에 해당함
    print(cartoon.get_text())

# 네이버웹툰의 html구조가 변경되어 더이상 작동하지않음
