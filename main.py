import math


if __name__ == '__main__':
    x = float(input())
    y = float(input())
    try:
        result = (1 - math.e**(x*y))/(0.7 * math.log10(math.fabs(1 - x**2)))
        print(result)
    except ValueError:
        print("Недопустимые значения")
