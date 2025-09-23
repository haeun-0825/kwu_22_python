# Collection type
#  - 여러값을 저장하고 싶은 경우 사용
#  - 리스트(List), 튜플(Tuple), 딕셔너리(Dictionary), 세트(Set)

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

# append(값)
list_a.append(4)  # 맨 마지막에 추가 [1, 2, 3, 4]
# insert(인덱스, 값)
list_a.insert(1, 5)  # 2번 인덱스에 5번 값 추가 [1, 5, 2, 3, 4]

# extend(): 리스트 병합
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
a = sorted(a)  # 오름차순
a = sorted(a, reverse=True)  # 내림차순

# Tip: 데이터 분석 or 인공지능 데이터 활용
#   → 원본 데이터는 유지, 복제 사용 
