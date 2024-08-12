def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


num = 3
print(is_prime(num))


# import math
# def factorial(num):
#     return math.factorial(num)

def factorial(numf):
    result = 1
    for i in range(2, numf + 1):
        result *= i
    return result


numf = 5
print(factorial(numf))
