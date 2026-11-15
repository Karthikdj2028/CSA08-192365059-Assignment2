# Q3 – Engineer a Vehicle Registration Number Validator

## Predictions before execution

| Raw input | Predicted normalised value | Prediction |
|---|---|---|
| `tn 09 ab 1234` | `TN09AB1234` | Valid |
| `KA-01-M-0007` | `KA01M0007` | Valid |
| `Tn09Ab1234` | `TN09AB1234` | Valid |
| `TN9AB1234` | `TN9AB1234` | Invalid: district is not two digits |
| `TN 22 1234 AB` | `TN221234AB` | Invalid: series is in the wrong position |
| `MH 12 P 9876` | `MH12P9876` | Valid |

## Validation logic

The normalisation function strips outside whitespace, converts to uppercase, then removes spaces and hyphens. Validation accepts only length 9 or 10. It checks `reg[0:2]` for two letters, `reg[2:4]` for two digits, `reg[4:-4]` for one or two letters, and `reg[-4:]` for four digits. The receipt function joins these four parts with spaces.

No regular expression is used in the main solution.

## String immutability

Strings are immutable: an existing string cannot be changed character by character. `text.upper()` creates and returns an uppercase string; it does not change the original variable unless the returned value is assigned. For `TN09A1234` (9 characters), `s[-4:]` is `1234` and `s[4:-4]` is `A`. For `TN09AB1234` (10 characters), those slices are `1234` and `AB`.

## Alternative: regular expression

`re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}", reg)` could check the whole normalised number in one expression. Both approaches take O(L) time for a string of length L. The string-slicing version makes each section visible and uses only the methods named in the assignment. A regular expression is compact but can be harder for a beginner to read; it may be easier to revise for more complex patterns once the syntax is understood.
