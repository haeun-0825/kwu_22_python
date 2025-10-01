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
