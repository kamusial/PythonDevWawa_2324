numbers = [9, 3, 7, 1, 3, 6]

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range((len(numbers) - 1)):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)
