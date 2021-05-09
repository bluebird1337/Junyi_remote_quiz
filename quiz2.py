def count_multiple(n):
    mul_of_3 = n / 3
    mul_of_5 = n / 5
    mul_of_15 = n / 15
    res = int(n - mul_of_3 - mul_of_5 + 2 * mul_of_15)
    return res

print(count_multiple(15))

