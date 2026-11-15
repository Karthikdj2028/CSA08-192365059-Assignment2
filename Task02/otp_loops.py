"""Q2: Demonstrate OTP attempt counting with while and for loops."""

EXPECTED_OTP = "482916"


def record_blank_entry():
    """Reserved for optional blank-entry logging; pass deliberately does nothing."""
    pass


def verify_with_while(entries, expected=EXPECTED_OTP, max_attempts=3):
    """Blank entries do not increase the number of used OTP attempts."""
    print("\nWHILE LOOP")
    attempts_used = 0
    entry_index = 0

    while attempts_used < max_attempts:
        if entry_index >= len(entries):
            print("No more sample entries.")
            return "Not completed"

        otp = entries[entry_index].strip()
        entry_index += 1

        if otp == "":
            print("Blank entry: not counted. Try again.")
            record_blank_entry()
            continue

        attempts_used += 1
        print(f"Attempt {attempts_used}: entered {otp}")
        if otp == expected:
            print("OTP correct. Access granted.")
            break
        print("Incorrect OTP.")
    else:
        print("Three wrong attempts. Account locked for 30 minutes.")
        return "Locked"

    return "Verified"


def verify_with_for(entries, expected=EXPECTED_OTP, max_attempts=3):
    """Use for-else; an inner while repeats a blank entry without using an attempt."""
    print("\nFOR LOOP WITH RANGE AND LOOP ELSE")
    entry_index = 0

    for attempt_number in range(1, max_attempts + 1):
        while True:
            if entry_index >= len(entries):
                print("No more sample entries.")
                return "Not completed"

            otp = entries[entry_index].strip()
            entry_index += 1

            if otp == "":
                print("Blank entry: not counted. Try again.")
                record_blank_entry()
                continue
            break

        print(f"Attempt {attempt_number}: entered {otp}")
        if otp == expected:
            print("OTP correct. Access granted.")
            break
        print("Incorrect OTP.")
    else:
        print("Three wrong attempts. Account locked for 30 minutes.")
        return "Locked"

    return "Verified"


def changed_condition_demo():
    """The security question adds two attempts, for a maximum of five."""
    security_answer_correct = True
    max_attempts = 3
    if security_answer_correct:
        max_attempts += 2
    print("\nCHANGED CONDITION")
    print("Security answer correct:", security_answer_correct)
    print("Allowed non-blank OTP attempts:", max_attempts)
    five_wrong_then_correct = ["111111", "222222", "333333", "444444", "482916"]
    verify_with_while(five_wrong_then_correct, max_attempts=max_attempts)
    verify_with_for(five_wrong_then_correct, max_attempts=max_attempts)
    return max_attempts


if __name__ == "__main__":
    while_result = verify_with_while(["", "111111", "222222", "482916"])
    for_result = verify_with_for(["", "111111", "222222", "333333"])
    print("While result:", while_result)
    print("For result:", for_result)
    changed_condition_demo()
