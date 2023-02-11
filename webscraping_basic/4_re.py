# 정규식 => 올바른 데이터의 형태를 확인하기 위해 이용하는것

# 주민등록번호
# 001221-1111111
# 이메일주소
# abcd@gmail.com
# => 데이터마다의 올바른 데이터의 형태를 확인하기 위해 정규식을 사용함

# 정규식 라이브러리 import
import re
# abcd, book, desk
# 기억는 데이터 => ca?e =? 3번째 글자가 기억이 나지 않는 상황
# caae, cabe, cace, ... 모든 숫자를 대입하면 오래걸림

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 => care, cafe, case | caffe (x)
# ^ (^de) : 문자열의 시작을 의미 => de로 시작하는 모든것 => desk, destination | fade (X)
# $  (se$) : 문자열의 끝을 의미 => se로 끝나는 모든것 => case, base | face(x)


# 매칭 성공여부에 따라 출력을 달리할수 있음
def print_match(m):
    if m:
        print("m.group():", m.group())  # 일치하는 문자열 반환
        print("m.string:", m.string)  # 입력받은 문자열 반환
        print("m.start():", m.start())  # 일치하는 문자열의 시작 index
        print("m.span():", m.span())  # 일치하는 문자열의 시작/ 끝 index
    else:
        print("매칭되지 않음")


# # 비교하려는 값 "case" => case와 p의 정규식 ca.e를 비교하여 부합하는지 확인
# m = p.match("cafe")
# print(m.group())  # 매치되지 않으면 에러가 발생
# e = p.match("caffe")
# print(e.group())  # 에러발생

# # 매칭 성공시 매칭값 출력
# print_match(m)

# m = p.match("careless")  # => 주어진 문자열의 처음부터 일치하는지 확인하기 때문에, care가 매칭됨
# print_match(m)  # => 출력값 :care

# m = p.search("good care")  # search : 주어진 문자열중에 일치하는게 있는지 확인
# # good care의 경우 care가 ca.e와 일치하므로 care가 출력됨
# print_match(m)

m = p.search("careless")  # search : 주어진 문자열중에 일치하는게 있는지 확인
print_match(m)
'''
결과값
m.group(): care
m.string: careless
m.start(): 0
m.span(): (0, 4)
'''
m = p.search("good care")  # search : 주어진 문자열중에 일치하는게 있는지 확인
print_match(m)  # good care의 경우 care가 ca.e와 일치하므로 care가 출력됨
'''
결과값
m.group(): care
m.string: good care
m.start(): 5
m.span(): (5, 9)
'''

lst = p.findall("good care cafe")  # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)
'''
결과값
['care', 'cafe'] # 일치하는 모든것을 리스트 형태로 반환해줌
'''

# 정리

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든것을 "리스트" 형태로 반환해줌

# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 => care, cafe, case | caffe (x)
# ^ (^de) : 문자열의 시작을 의미 => de로 시작하는 모든것 => desk, destination | fade (X)
# $  (se$) : 문자열의 끝을 의미 => se로 끝나는 모든것 => case, base | face(x)
