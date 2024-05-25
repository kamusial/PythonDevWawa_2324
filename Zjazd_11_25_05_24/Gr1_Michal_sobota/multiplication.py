def multimulti(numbers: list[int]) -> int:
    result = 1
    for number in numbers:
        result = result * number
    return result


def multiadd(numbers: list[int]) -> int:
    result = 0
    for number in numbers:
        result = result + number
    return result


print(multimulti([3, 5, 5]))
print(multiadd([3, 5, 5]))
