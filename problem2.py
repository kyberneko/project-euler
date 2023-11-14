result = 0
first, second = 0, 1

while second <= 4000000:
    if second % 2 == 0:
        result += second
    first, second = second, first + second

print(result)
