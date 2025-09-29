# for문
#  - 반복 횟수를 아는 경우 

# JAVA
# for(int i=0; i<9; i++) {
#     코드
# }

for num in [1, 2, 3]:  # 3번 반복
    print(num)
    
# range() 함수
#   - range(시작, 끝, 증감)
#   - default: 시작(0), 증감(+1)
#   - range(3)  끝이 3, 근데 끝은 -1해줘야함 → 0, 1, 2
#   - range(1, 4)                         → 1, 2, 3  
#   - range(2, 5, 2)                      → 2, 4
#   * 끝 인덱스의 마지막은 포함 X

# Tip: for문은 range()와 컬렉션 타입을 활용

# enumerate()
#   - 반복 횟수(index) 정보를 활용할 때
#   - 기본 for문에서는 반복횟수를 알 수 없음
for num in [1, 5, 9]:
    print(num)
for i, num in enumerate([1, 5, 9]):
    print(num)

# break & continue
#   - break: 반복문을 즉시 빠져 나오세요.
#   - continue: 즉시 다음 반복으로 넘어가세요.

# 구구단 2단
# 2x1=2
# 2x2=4
# ...
# 2x9=18
#for i in range(1, 10):
#    print(f"2x{i}={2*i}")

# 중첩 for문
#   - 구구단 2단 ~ 9단
#   - 첫번째 반복: 2단 ~ 9단
#   - 두번째 반복: 단별로 1 ~ 9

#for i in range(2, 10):  # 2~9
#   for j in range(1, 10):  # 1~9
#        print(f"{i}x{j}={i*j}")
