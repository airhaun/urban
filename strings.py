n = int(input())
password = ('')
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        sum_pair = i + j
        if n % sum_pair == 0:
            password += f'{i}{j}'

print(password)