"""
Count the number of steps of collatz conjecture for each int from 2 to 100
3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
"""


def collatz_iteration(number: int) -> int:
    """If number is even, divide it by 2. If it's odd, multiply by 3 and add 1."""
    if number % 2 == 0:
        return number // 2
    else:
        return number * 3 + 1


def collatz_conjecture(number: int) -> list[int]:
    steps = [number]
    while number != 1:
        number = collatz_iteration(number)
        steps.append(number)
    return steps


def main():
    for n in range(2, 101):
        steps = collatz_conjecture(n)
        print(len(steps))


if __name__ == '__main__':
    main()
    import time
    time.sleep(5)