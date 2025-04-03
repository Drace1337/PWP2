amount = int(input("Give numbers of Fibbonaci: "))
def fib(amount):
    a, b = 0, 1
    for _ in range(amount):
        yield a
        a, b = b, a+b

obj = fib(amount)
for _ in range(amount):
    print(next(obj))