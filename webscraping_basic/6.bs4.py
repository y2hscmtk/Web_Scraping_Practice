# 스크래핑을 위해 사용하는 라이브러리
# pip install beautifulsoup4
# 구분을 분석하기 위해
# pip install lxml
import requests
from bs4 import BeautifulSoup

# 네이버 웹툰 스크래핑
url = "https://comic.naver.com/webtoon"
res = requests.get(url)
res.raise_for_status()  # 문제 발생시 종료

# html문서를 lxml를 통해서 BeautifulSoup객체로 만듦
soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)  # title 태그를 가진 정보를 접근할수있게됨
# print(soup.title.get_text()) # 태그 없이 값만 확인
print(soup)  # soup 객체에서 첫번째로 발견되는 a태그의 정보가 출력됨
# print(soup.a.attrs)  # a element의 속성 정보를 반환
# print(soup.a["href"])  # a element의 href 속성 "값" 정보를 출력

# a 태그를 찾고 싶은데, 클래스 정보가 Nbtn_upload인것만 찾기
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# class가 "Nbtn_upload"인 어떤 element를 찾아줘
# print(soup.find(attrs={"class": "Nbtn_upload"}))

# # 인기 급상승 만화 찾기
# print(soup.find("li", attrs={"class": "rank01"}))
# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a)  # rank1의 a element정보만 가져오기
# print(rank1.a.get_text())  # rank1의 a element정보만 가져오기

# 다른 랭킹정보들도 얻고 싶을때 형제 정보(nex_sibling)
# 한번해서 정보가 표시되지 않을경우 줄바꿈이 되어있는 경우임 => nex_sibling을 한번 더하면 해결
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling

# rank3 = rank2.next_sibling.next_sibling

# print(rank3.a.get_text())
# # 이전 정보로 이동
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# 부모로 이동 => ol태그
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")  # li태그에 해당하는 다음 형제로 이동

# print(rank2.a.get_text())  # next_sibling을 두번 적는것을 방지할수 있음

# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# 한번에 형재들 가져오기
# print(rank1.find_next_siblings("li"))  # siblings => li태그를 가진 모든 형제들을 가져옴

# 네이버웹툰 페이지의 경우
# <a href ... text= ... >외모지상주의-430화 ..</a> => a태그 사이의 외모지상주의-430화.. 가 아래 함수의 text매개변수에 들어갈 값
webtoon = soup.find("a", text="외모지상주의-430화 통합된 4대크루 [1/2]")
print(webtoon)
