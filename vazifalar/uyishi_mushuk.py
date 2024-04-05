A, B, C = map(int, input().split())
if A < B and A < C or A > B and A > C:
    print("1-mushuk")
elif B < A and B < C or B > A and B > C:
    print("2-mushuk")
else:
    print("sichqon")