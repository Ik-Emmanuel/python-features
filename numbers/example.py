from decimal import Decimal, getcontext

def add_with_precision(a:float, b:float) -> Decimal:
    getcontext().prec = 20
    return Decimal(a) + Decimal(b)

result = add_with_precision(1.1, 2.2)
print(result)