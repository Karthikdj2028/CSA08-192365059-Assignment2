# Q2 – Loops that Count Attempts

## Main design

A `while` loop is natural because the number of input entries is not known in advance: blank input must be repeated without consuming one of the three attempts. Increase the counter only after receiving a non-blank OTP. Use `continue` for a blank entry and `break` when the OTP is correct.

The `for` version uses `range(1, max_attempts + 1)`. An inner `while` keeps asking until a non-blank entry is received, so a blank value does not consume an outer-loop attempt. The loop's `else` runs only when all attempts finish without `break`; that is where the account is locked.

`record_blank_entry()` contains `pass` to show a deliberate no-operation placeholder for a future audit/logging step. The function is called for a blank entry, but it does not change the attempt count.

## Counter bug

If the counter is increased before checking whether the input is blank, blank entries consume attempts. If it is increased after checking the OTP, an incorrect OTP may not be counted. Increase it exactly once for each non-blank OTP.

## Changed condition

If the security answer is correct, set `max_attempts = 5`; otherwise keep it at 3. Pass this value to either loop. Keep the attempt counter logic unchanged.

## Recursive alternative

A recursive function can call itself for the next input. It takes O(a) time for a attempts and O(a) stack space. The loop versions also take O(a) time but use O(1) extra space. For a small maximum of three or five attempts, recursion is unnecessary and a loop is easier to follow.
