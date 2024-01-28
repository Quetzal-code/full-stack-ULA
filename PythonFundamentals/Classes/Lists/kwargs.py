def sum_of(**kwargs):
    sum = 0
    for k , y in kwargs.items():
        sum += y
    return round(sum, 2)
print(sum_of(coffe = 2.88 , cake = 4.88 , pizza = 6.99))