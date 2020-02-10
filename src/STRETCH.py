import math

x = input("Enter a whole number: ")


def prime_tester(num):
    is_prime = True

    user_num = int(num)

    if num == 1 or num == 2:
        return is_prime
    else:
        for i in range(2, round(math.sqrt(user_num))):
            if user_num % i == 0:
                is_prime = False
                break
            else:
                is_prime = True
    return is_prime

print(prime_tester(x))
