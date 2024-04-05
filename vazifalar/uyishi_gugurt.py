N = int(input())
total_gugurts = 0
while N > 0:
    last_digit = N % 10 
    if last_digit == 0:
        total_gugurts += 6
    elif last_digit == 1:
        total_gugurts += 2
    elif last_digit == 2:
        total_gugurts += 5
    elif last_digit == 3:
        total_gugurts += 5
    elif last_digit == 4:
        total_gugurts += 4
    elif last_digit == 5:
        total_gugurts += 5
    elif last_digit == 6:
        total_gugurts += 6
    elif last_digit == 7:
        total_gugurts += 3
    elif last_digit == 8:
        total_gugurts += 7
    elif last_digit == 9:
        total_gugurts += 6
    N //= 10
print(total_gugurts)