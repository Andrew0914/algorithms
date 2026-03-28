import random
import time


def selection_sort(numbers: list[int], direction: str = 'asc') -> list[int]:
    inner_numbers = numbers.copy()
    for source_index in range(len(inner_numbers) - 1):
        target_index = source_index
        for destination_index in range(source_index + 1, len(inner_numbers)):
            if direction == 'asc' and inner_numbers[destination_index] < inner_numbers[target_index]:
                target_index = destination_index
            elif direction == 'desc' and inner_numbers[destination_index] > inner_numbers[target_index]:
                target_index = destination_index


        inner_numbers[source_index], inner_numbers[target_index] = inner_numbers[target_index], inner_numbers[source_index]

    return inner_numbers



my_numbers = random.sample(range(100000), 10000)
start_at = time.time()
sorted_numbers = selection_sort(my_numbers, 'asc')
end_at = time.time()

execution_time = (end_at - start_at)
if len(sorted_numbers) <= 20:
    print(my_numbers)
    print(sorted_numbers)
print(f"Sorted numbers: {len(sorted_numbers)}")
print(f"Execution time: {execution_time:.6f} seconds")
