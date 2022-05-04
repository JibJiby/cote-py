n = int(input())

arr = list(map(int, input().split()))

max_v = 0
answer = 0

# 그냥 max만 비교해도되는 이유가 이미 "정렬"되어 있기 때문에
for v in arr:
  if v > max_v:
    max_v = v
    answer += 1


print(answer)
