from collections import defaultdict


def solution(string: str) -> int:
    win_start, max_length, char_map = 0, 0, defaultdict(int)

    for win_end, right_char in enumerate(string):
        if right_char in char_map:
            win_start = max(win_start, char_map[right_char] + 1)

        char_map[right_char] = win_end
        max_length = max(max_length, win_end - win_start + 1)
    return max_length


def main():
    print(solution("aabccbb"))
    print(solution("abbbb"))
    print(solution("abccde"))


if __name__ == "__main__":
    main()
