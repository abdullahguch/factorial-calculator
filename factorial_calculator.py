def factorial(n):
    """
    Calculate the factorial of a non-negative integer n.

    :param n: The input integer.
    :type n: int
    :return: The factorial of n.
    :rtype: int
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
