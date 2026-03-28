finished: bool = False
NMAX = 1000


def is_a_solution(k: int, n: int) -> bool:
    return k == n


def construct_candidates(candidates: list[int]):
    candidates[0] = True
    candidates[1] = False
    return 2


def process_solution(a: list[int], k: int):
    print("{", end=" ")
    for i in range(1, k + 1):
        if a[i]:
            print(i, end=" ")
    print("}")


def backtrack(a: list[int], k: int, n: int):
    candidates = [0] * NMAX
    i: int = 0

    if is_a_solution(k, n):
        process_solution(a, k)
    else:
        k += 1
        ncandidates = construct_candidates(candidates)
        for i in range(ncandidates):
            a[k] = candidates[i]
            backtrack(a, k, n)


def get_subsets(n: int):
    a = [0] * (n + 1)
    backtrack(a, 0, n)


get_subsets(10)
