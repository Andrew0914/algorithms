import heapq


def find_kth_largest(nums: list[int], k: int) -> int:

    heap = []
    # k largest visible elements - make heap size need to just perform k ops
    for i in range(k):
        heapq.heappush(heap, nums[i])

    # avoid check the already elements in heap
    for i in range(k, len(nums)):
        # in nums[i] is bigger the heap root cannot be the kth largest
        if nums[i] > heap[0]:
            # these keep heap same k-size
            heapq.heappop(heap)
            heapq.heappush(heap, nums[i])

    # root contains the kth element because we keep heap k-size
    return heap[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(find_kth_largest(nums, k))
