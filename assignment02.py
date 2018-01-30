from random import *


def get_last(digits):
    total = 0

    even = (digits % 10) * 2
    even = (even // 10) + (even % 10)
    odd = (digits // 10) % 10

    total += even + odd
    digits = digits//100

    even = (digits % 10) * 2
    even = (even // 10) + (even % 10)
    odd = (digits // 10) % 10

    total += even + odd
    digits = digits // 100

    even = (digits % 10) * 2
    even = (even // 10) + (even % 10)
    odd = (digits // 10) % 10

    total += even + odd
    digits = digits // 100

    even = (digits % 10) * 2
    even = (even // 10) + (even % 10)
    odd = (digits // 10) % 10

    total += even + odd
    digits = digits // 100

    even = (digits % 10) * 2
    even = (even // 10) + (even % 10)
    odd = (digits // 10) % 10

    total += even + odd
    digits = digits // 100

    even = (digits % 10) * 2
    even = (even // 10) + (even % 10)
    odd = (digits // 10) % 10

    total += even + odd

    return total


def generate(digits):
    result = digits * 1000000 + randint(000000, 999999)
    last = get_last(result)
    return int(str(result) + str((10 - (last % 10)) % 10))


def main():
    digits = input("Enter first six digits of card:")
    print("Two valid numbers are: \n")
    print(generate(digits))
    print(generate(digits))
    print("\n")
    generated = generate(digits) + 6
    print("One invalid number is: \n")
    print(generated)


if __name__ == "__main__":
    main()

