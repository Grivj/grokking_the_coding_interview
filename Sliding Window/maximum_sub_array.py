"""
Problem Statement

Given an array of positive numbers and a positive number 'k', find the maximum
sum of any contiguous subarray of size 'k'.

Example 1:
    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:
    Input: [2, 3, 4, 1, 5], k=2
    Output: 7
    Explanation: Subarray with maximum sum is [3, 4].

"""


def max_sub_array_of_size_k(k: int, arr: list[int]) -> list[int]:
    """
    Sliding window approach
    O(n)
    """
    max_sum, win_sum, start = 0, 0, 0

    for i, end in enumerate(arr):
        win_sum += end
        if i >= k - 1:
            max_sum = max(max_sum, win_sum)
            win_sum -= arr[start]
            start += 1

    return max_sum


def main():
    arr_1 = [2, 1, 5, 1, 3, 2]
    arr_2 = [2, 3, 4, 1, 5]
    print(max_sub_array_of_size_k(3, arr_1))
    print(max_sub_array_of_size_k(2, arr_2))


if __name__ == "__main__":
    main()
