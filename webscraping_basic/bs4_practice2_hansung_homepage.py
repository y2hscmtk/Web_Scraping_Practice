# 9_bs4_coupang 실습 진행시 로딩이 너무 오래걸리는건지 soup객체를 만들수 없는 상황 발생
# 한성대학교 홈페이지를 통해 실습 진행
import requests
import re
from bs4 import BeautifulSoup

# 한성대학교 홈페이지
url = "https://www.hansung.ac.kr/hansung/8385/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGaGFuc3VuZyUyRjE0MyUyRmFydGNsTGlzdC5kbyUzRnBhZ2UlM0QxJTI2c3JjaENvbHVtbiUzRCUyNnNyY2hXcmQlM0QlMjZiYnNDbFNlcSUzRCUyNmJic09wZW5XcmRTZXElM0QlMjZyZ3NCZ25kZVN0ciUzRCUyNnJnc0VuZGRlU3RyJTNEJTI2aXNWaWV3TWluZSUzRGZhbHNlJTI2"
res = requests.get(url)
res.raise_for_status()  # 오류방지

soup = BeautifulSoup(res.text, "lxml")

# 모든 공지사항의 정보를 가져오기 위함
items = soup.find_all("td", attrs={"class": "td-subject"})

test = items[0].get_text()
# 양쪽의 공백 제거
print(test.strip())

for item in items:
    print(item.a.get_text().strip())


# # 정규식을 이용하여 td-num, td-sum, td-subject 등을 한번에 가져옴
# items = soup.find_all("tr")

# # print(items[1].find_all("td", attrs={"class": re.compile("^td-")}))
# # print(items[1].find_all("td", attrs={"class": "td-subject"}))
# print(items[1].find_all("span").get_text())


# for item in items:
#     print(item)
