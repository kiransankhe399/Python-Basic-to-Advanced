#Odd Thread Lib

def OddFactor(No):
    odd_factors = []
    sum_odd = 0

    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            odd_factors.append(i)
            sum_odd += i

    print("\nOddFactor Thread")
    print("Odd Factors:", odd_factors)
    print("Sum of Odd Factors:", sum_odd)