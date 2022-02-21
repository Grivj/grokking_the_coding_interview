"""
Problem Statement

Given an array of positive numbers and a positive number 'S', find the length of
the smallest contiguous subarray whose sum is greater than or equal to 'S'.
Return 0 if no such subarray exists.


"""


from math import inf


def smallest_subarray_with_a_greater_sum(s: int, arr: list[int]) -> int:
    win_sum, min_len, start = 0, inf, 0

    for i, end in enumerate(arr):
        win_sum += end
        while win_sum >= s:
            min_len = min(min_len, i - start + 1)
            win_sum -= arr[start]
            start += 1
    if min_len == inf:
        return 0
    return min_len


def main():
    print(smallest_subarray_with_a_greater_sum(7, [2, 1, 5, 2, 3, 2]))


if __name__ == "__main__":
    main()
