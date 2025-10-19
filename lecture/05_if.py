# 제어문(Control Language)
# 1. 조건문(Conidition Language)
#   - 특정 조건이 참(True)이면 ~해라
#   - if~else
#   - (switch~case) 파이썬은 없음

# 2. 반복문(Loop Language)
#   - 조건을 만족할 때까지 ~를 반복해라
#   - for: 반복 횟수를 아는 경우
#   - while: 반복 횟수를 모르는 경우


# if문
#  1. 특정 조건을 만족하는 경우 수행할 작업에 사용
#  2. 모든 조건은 boolean으로 표현 됨
#  3. 조건문의 경우 if, elif, else 블록 내 들여쓰기
#  4. 모든 블록문의 시작점은 : 추가

#  JAVA & C
# if (조건1) {
#     코드   
# } else if (조건2) {
#     코드
# } else {
#     코드
# }

if 2 > 0:
    pass
elif 3 > 0:
    pass
else:
    pass

# if문을 활용한 조합식
# 1. if
# 2. if~else
# 3. if~elif~elif
# 4. if~elif~else

# and: 모든 조건이 참(True)인 경우 참
# or: 하나의 조건이라도 참(True)인 경우 참

# 문제: 학점 계산기
score = 4.0

if score >= 4.1 and score <= 4.5:
    print("A")
elif score >= 3.6 and score <= 4.0:
    print("B")
elif score >= 3.1 and score <= 3.5:
    print("C")
elif score >= 2.6 and score <= 3.0:
    print("D")
else:
    print("F")
    
if 4.5 >= score >= 4.1:
    print("A")
elif 4.0 >= score >= 3.6:
    print("B")
elif 3.5 >= score >= 3.1:
    print("C")
elif 3.0 >= score >= 2.6:
    print("D")
else:
    print("F")

