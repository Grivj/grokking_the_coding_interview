from collections import defaultdict


def solution(k: int, string: str) -> int:
    start_idx, max_len, freq = 0, 0, defaultdict(int)

    for end_idx, end in enumerate(string):
        freq[end] += 1

        while len(freq) > k:
            start_char = string[start_idx]
            freq[start_char] -= 1
            if freq[start_char] == 0:
                del freq[start_char]
            start_idx += 1
        max_len = max(max_len, end_idx - start_idx + 1)
    return max_len


def main():
    print(solution(2, "araaci"))
    print(solution(1, "araaci"))
    print(solution(3, "cbbebi"))


if __name__ == "__main__":
    main()
