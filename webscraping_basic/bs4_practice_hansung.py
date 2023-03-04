import requests
from bs4 import BeautifulSoup

# 네이버웹툰의 홈페이지 구조가 변경됨에 따라 실습영상대로 하면 작동하지 않기때문에
# 학교 홈페이지 정보를 가져오는것으로 실습을 대체함

url = "http://cse.hansung.ac.kr/news?searchCondition"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
# print(soup.title.get_text())

# 공지사항 목록 모두 가져오기
# table에서 태그가 a인 모든 값 가져오기
announcement = soup.table.find_all("a")

for i in range(len(announcement)):
    print(str(i+1) + announcement[i].get_text())
