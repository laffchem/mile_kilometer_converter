def add(*args):
    return sum(args)

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(kwargs['add'])
    n += kwargs['add']
    n*= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)