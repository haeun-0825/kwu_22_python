# Collection type
#  - 여러값을 저장하고 싶은 경우 사용
#  - 리스트(List)[], 튜플(Tuple)() 튜플은 값을 한번 만들면 바꾸지 못함 -> 다시 만들어야 함(immuabale), (순서O)
#  - 딕셔너리(Dictionary){}, 세트(Set){} (순서X)

# * 순서가 있는 자료형 = 시퀀스 자료형: List, Tuple
# * 순서가 없는 자료형: Dict, Set


# 1. 리스트(List): 예시) 기차
#  - 시퀀스 자료형
#  - index 사용(슬라이싱 가능)
#  - [] 사용
#  - 정렬 가능
#  - mutable(생성 후 값 변경 가능)
#  - packing과 unpacking 가능
#  - 멤버함수 존재(append(), insert(), ...)
#  - 문자열을 리스트로 표현
str = "abc"  # = ["a", "b", "c"]
a = [1, 2, 3]  # packing
b, c, d = [1, 2, 3] # unpacking

# Quiz: aa와 bb의 값을 서로 교환하세요
aa = 5
bb = 3

# JAVA, C
temp = aa
aa = bb
bb = temp

# python
aa, bb = bb, aa  # 파이썬은 언패킹이 되기 때문에 가능

# 리스트 생성
list_a = [1, 2, 3]
list_b = []  # 빈 리스트 생성 가능
list_c = [1, "a", 3.14, True]  # 다양한 자료형을 담을 수 있음

# ()붙어있으면 함수, 멤버함수(많이 강조하심) = 리스트에만 쓸 수 있음
# append(값)
list_a.append(4)  # 맨 마지막에 추가 [1, 2, 3, 4]
# insert(인덱스, 값)
list_a.insert(1, 5)  # 2번 인덱스에 5번 값 추가 [1, 5, 2, 3, 4](수정되는게 아니라 뒤로 밀림, 수정되는건 update)

# extend(): 리스트 병합(extend=확장)
a = [1, 2, 3]
b = [2, 3, 4]
# a + b == a.extend(b)
a.extend(b)  # a에 b를 합치기 [1, 2, 3, 2, 3, 4]
a.append(b)  # [1, 2, 3, [2, 3, 4]]
print(a)

# remove(값): 값으로 삭제
list_a.remove(2)
# pop(인덱스): 인덱스로 삭제
temp = list_a.pop(0)  # 0번 인덱스의 값을 temp에 담고, 삭제하세요.

# index(값): 해당 값의 인덱스를 출력
list_a.index(2)  # 2라는 값의 인덱스 번호

# sort(): 원본값을 정렬 : 지양
# sorted(): 복제본을 정렬(원본값은 유지) : 지향
a = [95, 1, 3, 27, 5]
a = sorted(a)                # 오름차순
a = sorted(a, reverse=True)  # 내림차순

# Tip: 데이터 분석 or 인공지능 데이터 활용
#   → 원본 데이터는 유지, 복제 사용 


# 2. 튜플(Tuple)
#  - 시퀀스 자료형
#  - index 사용(슬라이싱 가능)
#  - () 사용, () 생략 가능
#  - 정렬 불가능
#  - immutable(생성 후 값 변경 불가능)
#  - packing과 unpacking 가능
#  - 멤버함수 존재하지 않음(정렬을 못하니까)

a = [1, 2, 3]  # List
b = (1, 2, 3)  # Tuple
c = 1, 2, 3    # Tuple
d = (5)        # Tuple
e = 5          # Int
f = 5,         # Tuple


# 3. 딕셔너리(Dictionary)  ex: 복주머니(마구잡이로 담아놓는)
#  - 순서가 없음(Non-시퀀스)
#  - 인덱스 없음
#  - 중괄호{} 사용
#  - {key:value} 데이터 구조 사용(키와 밸류가 한 쌍)
#  - key는 중복 불가
#  - value는 중복 가능
#  - value는 무조건 key로만 접근 가능(key가 인덱스 역할)
a = {
    "Korea": "Seoul",
    "Canada": "Ottwa",
    "USA": 3.14
}

# dict 항목 추가 및 변경
#  - 기존에 key가 존재하면 update(수정)
#  - 기존에 key가 존재하지 않으면 insert(삽입)
a["Japan"] = "Tokyo"  # insert
a["Japan"] = "Kyoto"  # update(key가 존재하니 update가 됨)

# dict 항목 삭제(key를 사용)
#  - del 키워드
#  - pop 함수 이용
del a["Japan"]  # 사용 금지
a.pop("Japan")  

# dict 병합
#  - update()
a = {"a":1, "b":2}
b = {"a":2, "c":5}
a.update(b)
print(a)  # {"a":2, "b":2, "c":5}

# clear()
#  - 딕셔너리의 모든 값을 초기화
a.clear()

# in()
#  - dict안에 key가 존재하는지 확인
print("japan" in a)

# value Access  a에서 japan을 꺼내오세요
print(a["japan"])      # "japan" key 없으면 오류
print(a.get("japan"))  # "japan" key 없으면 None 반환 (지향)

# 모든 key, value 접근
#  - keys()   : key만 추출
#  - values() : value만 추출
#  - items()  : key+value 추출(튜플 타입)
print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))  # list() 로 타입 변경하는걸 추천, 안할 시 타입을 지맘대로 꺼냄


# 4. 세트(Set) (중복값을 제거하고 싶을때 사용)
#  - 순서 없음, 인덱스 없음
#  - {} 사용 (순서가 없으면 다 {}...)
#  - 수학의 집합
#  - 중복값을 허용하지 않음(중요)
set_a = {1, 2, 3, 2, 2, 2, 2, 2}  # Set {1, 2, 3} (중복값을 지워버림)
aa = {}  # 딕셔너리

list_c = [1, 2, 3, 2, 3, 4, 5]  # 리스트
set(list_c)  # 세트(중복값 제거) {1, 2, 3, 4, 5}
list(set(list_c))  # [1, 2, 3, 4, 5]  ← 이거 외우래
