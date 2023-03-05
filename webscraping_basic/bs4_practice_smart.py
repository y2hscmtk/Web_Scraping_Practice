# bs4 웹 스크래핑 연습 3
# 비교과프로그램 목록 가져오기 => 스마트자기관리 시스템
import re
import requests
from bs4 import BeautifulSoup

url = "https://hsportal.hansung.ac.kr/ko/program"
res = requests.get(url)
res.raise_for_status()  # 오류방지

soup = BeautifulSoup(res.text, "lxml")