def two_positive_numbers(a, b, c):
    positive_num = sum(1 for num in [a, b, c] if num > 0)
    return positive_num == 2

print(two_positive_numbers(2, 4, -3))
print(two_positive_numbers(-4, 6, 8))
print(two_positive_numbers(4, -6, 9))
print(two_positive_numbers(-4, 6, 0))
print(two_positive_numbers(4, 6, 10))
print(two_positive_numbers(-14, -3, -4))