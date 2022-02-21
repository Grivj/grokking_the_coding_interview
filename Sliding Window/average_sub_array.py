"""
2. Pattern: Sliding Window

Given an array, find the average of all  subarrays of 'K' contiguous elements in
it.

Example:
    Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

Here, we are asked to find the average of all subarrays of '5' contiguous
elements in the given array. Let's solve this:

For the first 5 numbers (subarray from index 0-4), the average is: (1+3+2+6-1)/5
=> 2.2 The average of next 5 numbers (subarray from index 1-5) is: (3+2+6-1+4)/5
=> 2.8 For the next 5 numbers (subarray from index 2-6), the average is:
(2+6-1+4+1)/5 => 2.4
"""


def find_averages_of_subarrays_1(K, arr):
    """
    Brute-force approach.
    O(n * K)
    """
    result = []
    for i in range(len(arr) - K + 1):
        _sum = 0.0
        for j in range(i, i + K):
            _sum += arr[j]
        result.append(_sum / K)

    return result


def find_averages_of_subarrays_2(K, arr):
    """
    Sliding window approach
    O(n)
    """
    window_sum, window_start, result = 0.0, 0, []
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= K - 1:
            result.append(window_sum / K)
            window_sum -= arr[window_start]
            window_start += 1

    return result


def main():
    array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    K = 5
    result_1 = find_averages_of_subarrays_1(K, array)
    result_2 = find_averages_of_subarrays_2(K, array)
    print("Brute-force: " + str(result_1))
    print("Sliding window: " + str(result_2))


if __name__ == "__main__":
    main()
