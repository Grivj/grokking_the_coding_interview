def solution(k: int, arr: list[int]) -> list[int]:
    max_sum, win_sum, start = 0, 0, 0

    for i, end in enumerate(arr):
        win_sum += end
        if i >= k - 1:
            max_sum = max(max_sum, win_sum)
            win_sum -= arr[start]
            start += 1

    return max_sum


def main():
    print(solution(3, [2, 1, 5, 1, 3, 2]))
    print(solution(2, [2, 3, 4, 1, 5]))


if __name__ == "__main__":
    main()
