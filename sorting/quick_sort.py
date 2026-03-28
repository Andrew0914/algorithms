import random
import time

def quick_sort(numbers):
    if len(numbers) < 2:
        return numbers
    else:
        pivot = numbers[0]
        less = [num for num in numbers[1:] if num <= pivot]
        greater = [num for num in numbers[1:] if num > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

numbers = random.sample(range(10000), 10000)

my_numbers = random.sample(range(10000000), 10000000)
start_at = time.time()
sorted_numbers = quick_sort(my_numbers)
end_at = time.time()

execution_time = (end_at - start_at)
if len(sorted_numbers) <= 20:
    print(my_numbers)
    print(sorted_numbers)
print(f"Sorted numbers: {len(sorted_numbers)}")
print(f"Execution time: {execution_time:.6f} seconds")
