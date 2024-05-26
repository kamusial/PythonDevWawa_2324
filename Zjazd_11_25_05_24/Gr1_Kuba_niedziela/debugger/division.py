import random

for i in range(10):
    divident, divisor = random.randint(100, 200), random.randint(0,3)
    result = divident / divisor
    print(f"Operacja: {divident}/{divisor} z wynikiem {result}.")