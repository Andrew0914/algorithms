from heapq import heappop, heappush


def nth_ugly_number(n: int) -> int:
    ugly_numbers = set([1])
    heap = [1]
    for _ in range(n - 1):
        curr = heappop(heap)
        for factor in [2, 3, 5]:
            if factor * curr not in ugly_numbers:
                heappush(heap, factor * curr)
                ugly_numbers.add(factor * curr)

    return heap[0]


nth_ugly_number(7)
