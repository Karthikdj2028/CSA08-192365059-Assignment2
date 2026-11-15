"""Q3: Normalise, validate and format vehicle registration numbers."""


def normalise(text):
    """'tn 09 ab 1234' -> 'TN09AB1234' (remove spaces/hyphens and uppercase)."""
    return text.strip().upper().replace(" ", "").replace("-", "")


def is_valid(reg):
    """Check state, district, series and final four digits using slicing."""
    if len(reg) != 9 and len(reg) != 10:
        return False

    state = reg[0:2]
    district = reg[2:4]
    series = reg[4:-4]
    last_four = reg[-4:]

    if not state.isalpha():
        return False
    if not district.isdigit():
        return False
    if len(series) != 1 and len(series) != 2:
        return False
    if not series.isalpha():
        return False
    if not last_four.isdigit():
        return False
    return True


def format_receipt(reg):
    """Format a valid registration as four readable groups."""
    if not is_valid(reg):
        return "INVALID"
    return reg[0:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


samples = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "Tn09Ab1234",
    "TN9AB1234",
    "TN 22 1234 AB",
    "MH 12 P 9876",
]

print("Q3 - VEHICLE REGISTRATION VALIDATION")
print(f"{'RAW INPUT':20} {'NORMALISED':12} {'RESULT':8} RECEIPT")
for raw in samples:
    reg = normalise(raw)
    result = "valid" if is_valid(reg) else "INVALID"
    receipt = format_receipt(reg)
    print(f"{raw:20} {reg:12} {result:8} {receipt}")

print("\nString examples:")
s9 = "TN09A1234"
s10 = "TN09AB1234"
print(s9, "last four:", s9[-4:], "series:", s9[4:-4])
print(s10, "last four:", s10[-4:], "series:", s10[4:-4])
