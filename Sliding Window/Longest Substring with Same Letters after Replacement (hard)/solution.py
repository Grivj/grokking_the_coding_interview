from collections import defaultdict


def solution(string: str, k: int) -> int:
    win_start, max_length, max_repeat_letter_count, char_freq = (
        0,
        0,
        0,
        defaultdict(int),
    )

    for win_end, right_char in enumerate(string):
        char_freq[right_char] += 1
        max_repeat_letter_count = max(max_repeat_letter_count, char_freq[right_char])
        if win_end - win_start + 1 - max_repeat_letter_count > k:
            left_char = string[win_start]
            char_freq[left_char] -= 1
            win_start += 1
        max_length = max(max_length, win_end - win_start + 1)
    return max_length


def main():
    print(solution("aabccbb", 2))
    print(solution("abbcb", 1))
    print(solution("abccde", 1))


if __name__ == "__main__":
    main()
