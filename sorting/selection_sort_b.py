import random
import time

def get_max(numbers):
    max_value = None
    for num in numbers:
        if max_value is None or num > max_value:
            max_value = num
    return max_value

def get_min(numbers):
    min_value = None
    for num in numbers:
        if min_value is None or num < min_value:
            min_value = num
    return min_value

def selection_sort(numbers: list[int], direction: str = 'asc') -> list[int]:
    numbers_copy = numbers.copy()  # Work with copy to preserve original
    sorted_array = []
    sorting_operation = get_min if direction == 'asc' else get_max

    while len(numbers_copy) > 0:
        num = sorting_operation(numbers_copy)
        sorted_array.append(num)
        if num is not None:
            numbers_copy.remove(num)

    return sorted_array

# Test the implementation
my_numbers = random.sample(range(100000), 10000)
print(f"Sorting {len(my_numbers)} numbers...")

start_at = time.time()
sorted_numbers = selection_sort(my_numbers, 'desc')
end_at = time.time()

execution_time = (end_at - start_at)
print(f"Sorted numbers: {len(sorted_numbers)}")
print(f"Execution time: {execution_time:.6f} seconds")
