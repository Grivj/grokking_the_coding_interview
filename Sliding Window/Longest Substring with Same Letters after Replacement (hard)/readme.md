# Problem Statement

Given a string with lowercase letters only, if you are allowed to replace no more than âkâ letters with any letter, find the length of the longest substring having the same letters after replacement.

## Example 1

```python
Input: String="aabccbb", k=2
Output: 5
```

> Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

## Example 2

```python
Input: String="abbcb", k=1
Output: 4
```

> Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

## Example 3

```python
Input: String="abccde", k=1
Output: 3
```

> Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
