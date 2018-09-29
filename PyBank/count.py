count = 0
for i in range(10):
    count = i + 1
print(count)

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length


# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))
print(average(range(12)))
