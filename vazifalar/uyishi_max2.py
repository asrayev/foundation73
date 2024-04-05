n = int(input())
arr = [int(input()) for _ in range(n)]
max1 = -1
max2 = -1
for num in arr:
    if num > max1:
        max1 = num
    arr.remove(max1)
    if max2 < num:
        max2 = num
print