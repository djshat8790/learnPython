def add(*args):
    addi = 0
    for n in args:
        addi += n
    return addi


print(add(1, 2, 3, 4, 5, 43))


def calculate(**kwargs):
    print(kwargs)


print(calculate(sum=3))
