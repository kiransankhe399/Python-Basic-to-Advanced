#Even Factors Lib


def EvenFactor(No):
    even_factors = []
    sum_even = 0

    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            even_factors.append(i)
            sum_even += i

    print("Even Factors:", even_factors)
    print("Sum of Even Factors:", sum_even)
