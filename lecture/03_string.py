# 문자열의 이해(String)

# 1. 문자열 인덱스(index)
#  - 문자열은 각 문자마다 순서(인덱스)가 있음
#  - 첫번째 문자부터 마지막 문자까지 순차적으로 인덱스
#  - 인덱스 시작은 0
#  - 인덱스는 공백 포함
print("python")

# 2. 문자 추출
#  - 인덱스를통해 문자(문자열X) 추출
#  - 인덱스 범위를 벗어나면 오류
lang = "Python"  # 시험문제 내기 딱 좋다
print(lang[0])  # P
print(lang[2])  # t
# print(lang[10])  # IndexError: string index out of range

# 3. 역 인덱스(Reverse index)
#  - 인덱스(좌 → 우, 0 시작)
#  - 역 인덱스(우 → 좌, -1 시작)
print(lang[-1])  # n
print(lang[-3])  # h

# 4. 문자열 추출(슬라이싱)
#  - lang[0]: 문자 추출
#  - lang[0:3]: 문자열 추출(슬라이싱)
#  - 문자열 슬라이싱의 끝 인덱스 값 -1
#  - [시작:끝]
msg = "Python is all you need"
print(msg[0:6])  # 0~5, Python
print(msg[:6])  # 시작 생략(처음부터)
print(msg[3:])  # 끝 생략(끝까지)
print(msg[:])  # 시작, 끝 생략(처음부터 끝까지)
# 예: email 가입
#  kwu123@kwu.ac.kr 가입

# 5. 문자열 함수(꼭 알고 계셔야 겠죠?)
str = "Hello World"

# 5-1. Len(): 문자열 길이
print(len(str))  # 11(길이), 인덱스(0~10)

# 5-2. upper() and lower() : 대소문자 변경
print(str.upper())  # 대문자 변경
print(str.lower())  # 소문자 변경

# 5-3. replace(): 문자열 내의 특정 문자 치환
print(str.replace("H", "J"))  # Jello World

# 5-4. split(): 구분자를 기준으로 문자열 분할
print(str.split())  # Default(공백을 기준으로 쪼개짐) → "Hello", "World"
print(str.split("o"))  # "Hell", "W", "rld" (구분자 문자는 나오지 않음)

# 5-5. strip(): 문자열의 좌우공백 제거
print(str.strip())

# 5-6. in(): 특정 문자열 포함하는지 확인(True. False)
print("Hello" in str)  # True

# 5-7. find() and rfind(): 문자열의 특정 문자의 인덱스 출력
print(str.find("o"))  # 4
print(str.rfind("o"))  # 7
print(str.find("World"))  # 6, 단어의 첫글자 인덱스

# 6. f-string
grade = 4
name = "전하은"

# 고전 방법
print("저는 광주여자대학교 AI미디어콘텐츠학과 {}학년 {} 입니다.".format(grade, name))

# 새로운 방법(f-string)
print(f"저는 광주여자대학교 AI미디어콘텐츠학과 {grade}학년 {name} 입니다.")



# 숙제 - 1
a = "abc123@gmail.com"
b = "ter@naver.com"
c = "cherry@daum.net"
# @앞의 ID만 추출하는 코드 작성
# 정답: abc123, ter, cherry

print(a[:6])
print(b[:3])
print(c[:6])

print(a[:a.find("@")])
print(b[:b.find("@")])
print(c[:c.find("@")])

print(a.split("@")[0])
print(b.split("@")[0])
print(c.split("@")[0])

def my_id(email):
    at_index = email.find("@")
    return email[:at_index]
print(my_id(a))
print(my_id(b))
print(my_id(c))


# 숙제 - 2
d = "www.google.com"
e = "www.naver.com"
f = "www.daum.net"
# 가운데 도메인만 추출하는 코드 작성
# 정답: google, naver, daum

print(d[4:10])
print(e[4:9])
print(f[4:8])

print(d[d.find(".")+1:d.rfind(".")])
print(e[e.find(".")+1:e.rfind(".")])
print(f[f.find(".")+1:f.rfind(".")])

print(d.split(".")[1])
print(e.split(".")[1])
print(f.split(".")[1])

def domain(site_link):
    left_period=site_link.find(".")
    right_period=site_link.rfind(".")
    return site_link[left_period+1:right_period]
print(domain(d))
