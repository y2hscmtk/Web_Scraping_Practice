# 터미널에서 pip install requests
import requests
headers = {
    "User-Agent:": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

url = "https://nadocoding.tistory.com"

# url에 접속할때, 내가 정의한 header값을 넘겨줌 => 404에러 방지용?
# res = requests.get(url,headers=headers)
res = requests.get(url)
res.raise_for_status()

# 접속하는 브라우저의 타입에 따라 user agent가 다름

# 불러온 데이터를 파일로 만들어서 확인
with open("nanocoding.html", "w", encoding="utf-8") as f:
    f.write(res.text)  # 불러온 내용을 mygoogle.html파일g에 작성
