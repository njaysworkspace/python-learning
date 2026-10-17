# DATE: 17 OCT 2026
def square_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number ** 2
    return total
    
print(square_sum([1, 2, 2]))
