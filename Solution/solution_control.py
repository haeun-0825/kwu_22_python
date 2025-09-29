# Solution-1
# 리스트 a의 평균을 계산하고 출력하세요.
a = [1, 2, 3, 4, 5, 99, 87, 52, 2, 5, 4]

total = 0
for num in a:
    total += num
result = total / len(a)

print(f"평균: {result}")


# Solution-2
#   - 리스트에서 최소값과 최대값 찾기
c = [2, 5, 7, 1, 8]

num_min = c[0]
num_max = c[0]

for num in c:
    if num < num_min:
        num_min = num
    if num > num_max:
        num_max = num

print(f"최소값: {num_min}")
print(f"최대값: {num_max}")


c = [2, 5, 7, 1, 8]
c = list(set(c)).sort()

num_min = c[0]
num_max = c[-1]