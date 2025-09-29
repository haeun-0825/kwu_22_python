# while문
#   - 반복횟수를 모르는 경우
#   - 조건이 만족하는 동안 반복하세요.
#   - 조건(True) → 무한루프 → 조건 + break문

while True:
    if 3 > 0:
        break
    
# 구구단 2단 while문
for i in range(1, 9):
    print(f"2x{i}={2*i}")
    
i = 1
while i < 10:
    print(f"2x{i}={2*i}")
    i += 1  # i = i+1
    
