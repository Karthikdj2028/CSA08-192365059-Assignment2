"""Q6: Count ways to climb n steps using 1-step or 2-step moves."""

from functools import lru_cache
import sys

naive_calls = 0
memo_calls = 0


def ways_naive(n):
    """Plain recursive solution; this repeats many function calls."""
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return 1
    return ways_naive(n - 1) + ways_naive(n - 2)


@lru_cache(maxsize=None)
def ways_memo(n):
    """Recursive solution that remembers answers already calculated."""
    global memo_calls
    memo_calls += 1
    if n <= 1:
        return 1
    return ways_memo(n - 1) + ways_memo(n - 2)


def ways_loop(n):
    """Iterative solution that keeps only the previous two answers."""
    if n <= 1:
        return 1
    previous_two = 1
    previous_one = 1
    for step in range(2, n + 1):
        current = previous_one + previous_two
        previous_two = previous_one
        previous_one = current
    return previous_one


print("ANSWERS FOR n = 1 TO 6")
for n in range(1, 7):
    print(f"n={n}: {ways_loop(n)} ways")

print("\nCALL COUNTS")
print("n | naive answer | naive calls | memo answer | memo calls")
for n in [10, 20, 25, 30]:
    naive_calls = 0
    naive_answer = ways_naive(n)

    ways_memo.cache_clear()
    memo_calls = 0
    memo_answer = ways_memo(n)

    print(f"{n:2} | {naive_answer:12} | {naive_calls:11} | {memo_answer:11} | {memo_calls:10}")

print("\nRECURSION LIMIT")
print("Current recursion limit:", sys.getrecursionlimit())
ways_memo.cache_clear()
memo_calls = 0
try:
    print("Memoised ways for 1000:", ways_memo(1000))
except RecursionError as error:
    print("RecursionError for memoised n=1000:", error)

try:
    print("Naive ways for 1000:", ways_naive(1000))
except RecursionError as error:
    print("RecursionError for naive n=1000:", error)

print("\nITERATIVE RESULT FOR n=1000")
print("ways_loop(1000) =", ways_loop(1000))
