# bs4 웹 스크래핑 연습 3
# 비교과프로그램 목록 가져오기 => 스마트자기관리 시스템
import re
import requests
from bs4 import BeautifulSoup

url_main = "https://hsportal.hansung.ac.kr/ko/program/all/list/all/"

# 5페이지의 정보를 계산
for page in range(1, 7):
    url = url_main + str(page)
    res = requests.get(url)
    res.raise_for_status()  # 오류방지

    soup = BeautifulSoup(res.text, "lxml")

    # 비교과 포인트, 마감일 정보
    point_info = soup.find_all("label", attrs={"class": "APPROACH_CLOSING"})
    # 제목 정보
    title_info = soup.find_all("b", attrs={"class": "title"})

    print(str(page) + "번째 페이지에 대한 정보입니다.")
    for i in range(len(point_info)):
        title = title_info[i].get_text()
        Dday, point = point_info[i].get_text().split("p")
        print(title)
        print("마감일: " + Dday + " 포인트: " + point)
    print("*************************************************")
