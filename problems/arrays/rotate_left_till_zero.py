from queue import Queue

def rotate_left_till_zero(numbers: list[int]) -> list[int]:
    queue = Queue()
    queue.set_queue(numbers)

    while queue.peek() != 0:
        removed = queue.remove()
        queue.insert(removed)


    queue.log()
