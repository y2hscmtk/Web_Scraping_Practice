# https://comic.naver.com/webtoon/list?titleId=799793
# 가우스 전자
from bs4 import BeautifulSoup
import requests
url = "https://comic.naver.com/webtoon/list?titleId=799793"

res = requests.get(url)
res.raise_for_status()  # 문제 발생시 종료

# html문서를 lxml를 통해서 BeautifulSoup객체로 만듬

# => 네이버웹툰의 구조적 문제로 인해 더이상 올바르게 작동하지 않음
soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class": "title"})

print(title=cartoons[0].a.get_text())
