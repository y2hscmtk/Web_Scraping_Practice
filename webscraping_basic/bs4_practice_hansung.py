import requests
from bs4 import BeautifulSoup

url = "http://cse.hansung.ac.kr/news?searchCondition"
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")
# print(soup.title.get_text())

# 공지사항 목록 모두 가져오기
announcement = soup.table.find_all("a")

for i in range(len(announcement)):
    print(str(i+1) + announcement[i].get_text())
