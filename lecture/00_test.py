# 1. 리스트 a의 모든 원소의 곱을 계산하여 출력하도록 빈칸을 완성하시오.
a = [1, 2, 3, 4]
result = 1
for num in a:
    result *= num  # *=
print(result)

# 2. 리스트 b에서 짝수의 개수를 세어 출력하도록 빈칸을 완성하시오.
b = [1, 2, 3, 4, 5]
count = 0
for num in b:
    if num % 2 ==0:
        count += 1  # count += 1
print(count)

# 3. 리스트 c에서 최대값이 위치한 인덱스 번호를 출력하도록 빈칸을 완성하시오.
c = [2, 7, 1]
max_val = c[0]
max_idx = 0
for i, num in enumerate(c):  # enumerate(c)
    if num > max_val:
        max_val = num
        max_idx = i
print(max_idx)

# 4. 문자열 s에서 대문자 'P'가 몇 개인지 세어 출력하는 코드를 작성하시오.
s = "PythonProgramming"

p_count = 0
for char in s:
    if char == "P":
        p_count += 1
print(p_count)

# 5. 딕셔너리 d의 모든 값(Value)의 합계를 출력하도록 빈칸을 완성하시오.
d = {"a": 10, "b": 20}
total = 0
for val in d.values():  # values()
    total += val
print(total)



# 6. 함수 내부에서 전역 변수 A의 값을 20으로 영구히 바꾸도록 func함수 내부에 들어갈 두 줄 코드를 작성하시오.
A = 10
def func():
    global A
    A = 20
func()
print(A)

# 7. 다음 코드의 최종 출력값을 예측하고, 그 이유를 서술하시오.
X = 5
def test():
    Y = 10
    X = Y + 1
    print(f"함수 내부: {X}")  # 함수 내부: 11
test()
print(f"최종 출력: {X}")  # 최종 출력: 5
# test()함수를 수행하며 선언된 지역변수 Y = 10, X = Y + 1은 함수 내부에서만 수행되며 print()함수를 통해 출력했을 때 "함수 내부: 11"이라는 출력을 보이고,
# 함수가 수행이 끝난 시점에서 선언된 지역변수들은 소멸된다. 그러기에 함수 밖에서 수행한 print()함수에서는 {X}에 전역변수 X = 5가 할당되어 "최종 출력: 5"라는 출력을 보인다.

# 8. 다음 코드는 오류가 발생한다. 오류가 발생하는 이유를 쓰시오.
total = 0
def add(n):
    total += n  # total = total + 5
add(5)
print(total)
# 함수내에 종료시에 반환되는 return 값이 없기 때문이다.(모르겟음.)

# 9. 다음 코드 실행 후, 함수 외부에서 B 변수에 접근하려 할 때 발생하는 오류명을 쓰시오.
def func():
    B = 100
func()
# print(B)
# (이것도 모르겟음)

# 10. 다음 코드에서 print(A)의 최종 출력값을 예측하고, 그 이유를 변수 범위를 들어 설명하시오.
A = 10
def change(A):
    A = 20
change(A)
print(A)
# 출력값은 10이며, 전역변수로 A = 10이라고 선언이 되었으며, change()함수에서 A = 20이라고 지역변수를 선언하였지만 print()함수를 이용하진 않은 상태에서 함수가 종료되었고, 함수가 끝난 뒤에 print(A) 출력함수를 실행하였기에 전역변수 A = 10이 할당이 되어 10을 출력하게 된다.



# 11. 다음 코드를 실행했을 때 발생하는 오류명을 쓰시오.
t = (1, 2, 3)
t[0] = 5
print(t)
# 오류명은 모르겠지만, t의 자료형은 튜플(Tuple)이며 값의 변경이 불가한 immutable자료형이기 때문에 오류가 발생한다.

# 12. 리스트 a를 오름차순으로 정렬한 후 원본 a를 출력하도록 빈칸을 완성하시오.
a = [3, 1]
a.sort()
print(a)

# 13. 빈 딕셔너리가 아닌 빈 세트(set)를 생성하는 코드를 작성하시오.
a = set()

# 14. 문자열 "ABCDE" 에서 가운데 문자 C만 추출하는 슬라이싱 코드를 작성하시오
s = "ABCDE"
print(s빈칸)  # [2]

# 15. 딕셔너리 d에서 items() 함수를 통해 얻은 항목 중, 키(key)만 추출하도록 빈칸을 완성하시오.
d = {"k": 1, "v": 2}
print(list(d.items())[0][0])

# 16. 리스트 a에 값이 삽입된 후 a를 출력하는 코드를 작성하시오.(힌트: 인덱스가 범위를 벗어나도 오류가 발생하지 않음)
a = [1, 2]
# 몰루겟어여

# 17. 문자열 "a, b, c"를 쉼표 , 로 분리한 후 두 번째 문자 (b)를 출력하도록 빈칸을 완성하시오.
s = "a, b, c"
print(s.split(",")[1])

# 18. 세트 s에 값 2가 포함되어 있지 않은지 확인하여 True 또는 False를 출력하는 코드를 작성하시오.
s = {1, 3, 5}
print(2 not in s)

# 19. 함수 f가 파라미터를 동적으로 받도록 튜플 형태로 처리하는 코드를 작성하시오.
def f():
    print(*args)
    
# 몰루겠어여

# 20. 딕셔너리 d에서 키 "v"가 없을 때, 기본값으로 99를 반환하도록 빈칸을 완성하시오.
d = {"k": 1}
print(d.get("v", 99))