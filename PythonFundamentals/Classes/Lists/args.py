def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum_of(3, 5, 6, 7, 9))