# 터미널에서 pip install requests
import requests
# 네이버로부터 request정보를 가져옴
res = requests.get("https://www.google.com/")
# html문서를 가져오는데 성공했다면 문제없이 진행되고, 그렇지 않을경우 에러를 일으킴
res.raise_for_status()  # 4번과 6번줄의 코드는 쌍으로 함께쓴다고 생각할것
# 6번 줄의 코드는 아래 주석과 같은 효과를 낸다.

# print("응답코드:", res.status_code)  # status_code가 200이면 정상적으로 리퀘스트정보를 가져온것

# if res.status_code == requests.codes.ok:  # ok는 code 200과 동일
#     print("정상입니다.")
# else:
#     print("스크래핑 불가능. [에러코드 : ", res.ststus_code, "]")

print(len(res.text))  # 가져온 글자 수 확인
print(res.text)

# 불러온 데이터를 파일로 만들어서 확인
with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)  # 불러온 내용을 mygoogle.html파일에 작성
