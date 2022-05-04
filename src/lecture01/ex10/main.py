word, c = input().split()

c_index = None

answer = []

# 왼쪽에서부터
for v in word:
  if c_index is None:
    if v == c:
      pass