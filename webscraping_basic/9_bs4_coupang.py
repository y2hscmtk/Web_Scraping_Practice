import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

print(res.text)

# 로딩 시간이 너무 오래걸리는 관계로 패스

# 기억해둘것

# find명령을 통해 item에서 상품정보를 하나씩 탐색할수있다.
# 이미 find_all을 통해 가져온 items목록에서 하나의 상품 데이터에서 값을 추출할때는 find_all대신 find를 사용해야함
# 추가로 만약 특정 상품을 제외하고 싶을때는 특정 태그가 존재하는지 확인하여 존재한다면 다음 요소로 넘어가게 할 수 있다.
'''
for item in items:
    ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("광고상품제외")
        continue
    name = item.find("div",attrs={"class":"name"}).get_text() # 제품명
    ...
    ...

'''
