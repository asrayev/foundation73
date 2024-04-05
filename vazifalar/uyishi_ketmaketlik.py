n = int(input())
a = (2 ** (2 * n + 1) - 2 ** (n + 1) + 1) % 5 == 0
b = (2 ** (2 * n + 1) + 2 ** (n + 1) + 1) % 5 == 0
if a:
    print("A")
elif b:
    print("B")
