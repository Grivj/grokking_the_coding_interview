from collections import defaultdict


def solution(array: list[int], k: int) -> int:
    win_start, max_length, max_ones_count = 0, 0, 0

    for win_end, right_int in enumerate(array):
        if right_int == 1:
            max_ones_count += 1

        if (win_end - win_start + 1 - max_ones_count) > k:
            if array[win_start] == 1:
                max_ones_count -= 1
            win_start += 1
        max_length = max(max_length, win_end - win_start + 1)
    return max_length


def main():
    print(solution([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(solution([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


if __name__ == "__main__":
    main()
