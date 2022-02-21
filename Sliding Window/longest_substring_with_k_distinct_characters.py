"""
Problem Statement

Given a string, find the length of the longest substring in it with no more than
K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:
    Input: String="araaci", K=2 Output: 4 Explanation: The longest substring with no
    more than '2' distinct characters is "araa".
Example 2:
    Input: String="araaci", K=1 Output: 2 Explanation: The longest substring with no
    more than '1' distinct characters is "aa".
Example 3:
    Input: String="cbbebi", K=3 Output: 5 Explanation: The longest substrings with
    no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

from collections import defaultdict


def longest_substring_with_k_distinct_characters(k: int, string: str) -> int:
    start, max_len, freq = 0, 0, defaultdict(int)

    for i, end in enumerate(string):
        freq[end] += 1

        while len(freq) > k:
            start_char = string[start]
            freq[start_char] -= 1
            if freq[start_char] == 0:
                del freq[start_char]
            start += 1
        max_len = max(max_len, i - start + 1)
    return max_len


def main():
    print(longest_substring_with_k_distinct_characters(2, "araaci"))


if __name__ == "__main__":
    main()
