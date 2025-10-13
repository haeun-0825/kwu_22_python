# 함수(method, function)
#   - 어떤 일을 수행하는 코드 묶음
#   - 반복적으로 동작해야하는 일들!

# ** 함수 개발 가이드라인 **
#   1. 함수 이름 및 내용
#     - 함수 이름에 함수의 역할과 의도 명확히 드러낼 것!
#     - 함수 내용은 가능하면 짧게 작성(최소 기능 단위)
#   2. 함수의 역할
#     - 하나의 함수에 유사한 역할의 코드만 작성
#     - 하나의 함수는 한가지 기능만 명확히 정의

# ** 함수의 종류 **
#   1. 내장함수(Built-in function)
#     - Python에서 기본적으로 제공하는 함수
#     - print(), type(), ...
#   2. 외장함수
#     - Library: 다른 사람(기업)이 개발한 코드 묶음 (라이브러리 안에 외장함수가 많이 있다.)
#     - 다운로드 후 호출(import)
# import pandas as pd
# pd.read_excel()
#   3. 사용자정의함수
#     - 개발자가 직접 만들어서 사용하는 함수

# ** 함수 이름 규칙 **
#   - snake_case

# ** 함수 정의 **
# 1. 기본 문법
#   def 함수명(parameter1, parameter2, ...):
#       실행문
#       return 반환값
# 2. def 키워드(define)
# 3. 함수의 입력값: (parameter1, ...)
# 4. 함수 종료: return
# 5. 함수 종료 및 반환: return 반환값
# 6. parameter와 return은 생략 가능

# 가. 함수 정의
def sum_two_value(x: int, y: int)  -> int:  # Type Hint
    n = x+y
    return n  # return: 호출했던 곳으로 돌아감

print("Hello")
result = sum_two_value(5, 10)  # 나. 함수호출 후 변수로 바뀜
print(result)

# ** 인자, 매개변수, parameter **
#   - 함수에 전달되는 입력값
#   - 함수 정의문과 호출문의 인자 갯수는 동일
#   - 인자가 여러개인 경우 순서대로 전달
#   - default parameter
#     def test(a, b, c=3):     (O)
#     def test(a=3 ,b , c):    (X)  
#     def test(a, b=15, c=3):  (O)  <- 뒤에서부터 채워야 함

# ** return **
#   - 함수 종료하고 호출했던 곳으로 돌아감
#   - 함수 블록 내에서 return문 다음에 코드가 와도 되지만,
#     실행되지는 않음.
#   - return 반환값: 호출했던 곳으로 돌아가면서 반환값을 전달
#   - return: 호출했던 곳으로 돌아가면서 None값을 전달

# ** 타입 힌트(Type Hint) **
#   - parameter와 return값의 타입을 미리 적어두기
#   - 안적어도 실행하는데 문제 없음(단순 가독성)

# ** 변수의 범위 **
#   - 변수가 참조 가능한 코드상의 범위를 명시
#   - 함수내의 변수는 자신이 속한 코드 블록이 종료되면 소멸  *중요*
#   - 특정 코드블록에서 선언된 변수를 "지역변수"
#   - 가장 상단에 정의되어 프로그램 종료 전까지 유지되는 변수를 "전역변수"
#   - 파이썬 코드 내에서는 동일한 이름의 변수명 사용불가
#     단, 지역변수와 전역변수의 경우 동일한 이름 사용 가능
#     → 변수의 사용 범위가 다르기 때문
#   - 동일한 이름의 지역변수와 전역변수가 존재하는 경우 
#     가까운(지역변수) 변수가 우선순위 높음

num1 = 10  # 전역
num2 = 20  # 전역

def test(num1):
    num2 = 50  # 지역
    print(num1, num2)  # 30 50 출력
    return

test(30)
print(num1, num2)  # 10 20 출력

# ** 가변 길이 인자 **
#   - 전달되는 parameter 개수가 고정적이지 않은 경우
#   - print(), format() 등

print(1)
print(1, 2)
print(1, 2, 3)

# 1) *args: tuple
def test(*args):
    for item in args:
        print(item)
test(10, 20, 30)

# 2) **kwargs: dict
def test2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
test2(a=1, b=2, c=3)
# *: 튜플 / **: 딕트 타입으로 전달
