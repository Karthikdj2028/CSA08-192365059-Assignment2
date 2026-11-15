"""Q2 alternative: a small recursive OTP attempt demonstration."""


def verify_recursive(entries, expected, attempts_used=0, entry_index=0, max_attempts=3):
    """Use recursion to process the next non-blank entry."""
    if attempts_used >= max_attempts:
        return "Locked for 30 minutes"
    if entry_index >= len(entries):
        return "Not completed"

    otp = entries[entry_index].strip()
    if otp == "":
        return verify_recursive(entries, expected, attempts_used,
                                entry_index + 1, max_attempts)
    if otp == expected:
        return "Verified"
    return verify_recursive(entries, expected, attempts_used + 1,
                            entry_index + 1, max_attempts)


print(verify_recursive(["", "111111", "222222", "333333"], "482916"))
print("Time: O(a) for a non-blank attempts; recursion stack space: O(a).")
