# Q6 – Recursion and Its Limits

## Recurrence and base cases

For zero or one step there is one way: `ways(0)=1` and `ways(1)=1`. For n at least 2, the first move can take one step or two steps, so `ways(n)=ways(n-1)+ways(n-2)`.

## Plain recursion and repeated work

The call tree for n=5 is included in `call_tree_n5.md`. The same smaller n values appear in more than one branch. Plain recursion takes O(phi^n) time (exponential growth) and O(n) call-stack space due to the maximum recursion depth.

## Memoisation

The `lru_cache` decorator stores each calculated argument/result pair. Each n value from 0 to n is computed once, so the time is O(n). The cache and recursion stack use O(n) space. For n=25, the expected result is 121393; a memoised run normally executes the function body 26 times (for n=25 down to n=0), while plain recursion makes 242785 calls.

## Iterative alternative

A loop retains only the previous two results. It takes O(n) time and O(1) extra space. It is the simplest deployment choice for n=1,000 because it avoids recursion depth limits and does not need an O(n) cache.

## Recursion limit

`sys.getrecursionlimit()` reports the interpreter's current recursion limit (commonly around 1,000). A memoised recursion for n=1,000 can still raise `RecursionError`; memoisation reduces repeated calculations but does not remove the recursive call depth. Raising the recursion limit can risk exhausting the C stack and is not the preferred fix for a production program. Use the iterative loop for the 1,000-step requirement. The program attempts the recursive call inside `try/except` and then prints the iterative answer.

## Required call counts

Run `python3 Task06/stair_ways.py` on your Mac and copy the raw call counts for n=10,20,25,30 into the report. The values should be deterministic; execution time is not required for this question.
