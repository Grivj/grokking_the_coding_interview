from collections import defaultdict


def solution(fruits: list[str]) -> int:
    start_idx, max_length, fruit_frequency = 0, 0, defaultdict(int)

    for end_idx, right_fruit in enumerate(fruits):
        fruit_frequency[right_fruit] += 1

        while len(fruit_frequency) > 2:
            left_fruit = fruits[start_idx]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            start_idx += 1
        max_length = max(max_length, end_idx - start_idx + 1)
    return max_length


def main():
    print(solution(["A", "B", "C", "A", "C"]))
    print(solution(["A", "B", "C", "B", "B", "C"]))


if __name__ == "__main__":
    main()
