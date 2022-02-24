from math import inf


def solution(s: int, arr: list[int]) -> int:
    win_sum, min_len, start_idx = 0, inf, 0

    for end_idx, integer in enumerate(arr):
        win_sum += integer
        while win_sum >= s:
            min_len = min(min_len, end_idx - start_idx + 1)
            win_sum -= arr[start_idx]
            start_idx += 1
    if min_len == inf:
        return 0
    return min_len


def main():
    print(solution(7, [2, 1, 5, 2, 3, 2]))
    print(solution(7, [2, 1, 5, 2, 8]))
    print(solution(8, [3, 4, 1, 1, 6]))


if __name__ == "__main__":
    main()
