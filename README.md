# CSA08-192365059-Assignment2

**Assignment:** Assignment 2 – Control Flow, Strings and Functions  
**Course:** CSA08 – Python Programming  
**Student:** S Karthikeyan  
**Register Number:** 192365059  
**Nature:** Individual  
**Platform:** Windows 10  
**Python command:** `python`  
**Python version used:** Python 3.11.6

**GitHub repository:** https://github.com/Karthikdj2028/CSA08-192365059-Assignment2

## Project overview

This project covers all seven questions in Assignment 2 using beginner-friendly Python: conditions, loops, string methods and slicing, functions, parameters, scope, recursion, memoisation and performance measurement.

| Folder | Assignment question | Main work |
|---|---|---|
| Task01 | Q1 – Decisions with Many Boundaries | Separate `if` versus `if-elif-else`, boundaries, `match-case`, lookup list |
| Task02 | Q2 – Loops that Count Attempts | `while`, `for`, blank OTP handling, `break`, `continue`, `pass`, loop `else`, recursion alternative |
| Task03 | Q3 – Vehicle Registration Validator | Normalising, validating and formatting strings without regular expressions |
| Task04 | Q4 – Building Long Text | `+=`, `join()`, f-strings, measurements at 1,000 / 10,000 / 200,000 lines |
| Task05 | Q5 – Functions, Parameters and Scope | Mutable default argument bug, corrected list handling, parameters and scope |
| Task06 | Q6 – Recursion and Its Limits | Naive recursion, memoisation, function-call counts, recursion limit and loop solution |
| Task07 | Q7 – Diagnose, Redesign and Validate | Streaming a large statement to a file and comparing it with the original builder |

Each task folder contains Python source files or written analysis, a task README and an `evidence/` folder. Task04 and Task07 include raw CSV timing data.

## Python and libraries

- Python 3.11.6 on Windows 10, run with `python`.
- Third-party libraries: none.
- Standard-library modules used include `time`, `io`, `sys`, `functools`, `csv`, `os` and `tempfile`.
- `requirements.txt` is included. No `pip install` is needed.
- The `match-case` alternative in Q1 is supported by Python 3.11.6.

## Setup on Windows

Open the inner `CSA08-192365059-Assignment2` folder in VS Code. Select **Terminal → New Terminal**. Confirm the terminal is in the folder containing this README.

```powershell
python --version
git --version
pwd
```

Expected Python version:

```text
Python 3.11.6
```

## Run commands

Run these commands from the project root folder:

| Task | Command | What to check |
|---|---|---|
| Task01 | `python Task01/decisions.py` | Eight households, including 100 / 101 / 200 / 201 unit boundaries; compare separate `if` and `if-elif-else`. |
| Task02 | `python Task02/otp_loops.py` | While loop and for loop; blank entries do not consume attempts; loop `else` locks after three wrong attempts. |
| Task02 | `python Task02/recursive_otp_alternative.py` | Recursive alternative and its stack-space explanation. |
| Task03 | `python Task03/plate_validator.py` | Normalising, validation, six cases, receipt formatting and slicing. |
| Task04 | `python Task04/string_building.py` | `+=`, `join()` and f-string builders; three-run averages at 1,000 / 10,000 / 200,000 lines; writes `Task04/timings.csv`. |
| Task04 | `python Task04/string_alternatives.py` | StringIO and direct-file-writing alternatives. |
| Task05 | `python Task05/orders_and_scope.py` | Mutable default bug, independent orders for three customers, defaults tuple and scope examples. |
| Task06 | `python Task06/stair_ways.py` | Answers 1–6, function-call counts for 10 / 20 / 25 / 30, recursion-limit demonstration and iterative n=1,000 result. |
| Task07 | `python Task07/streaming_redesign.py` | Original versus streaming redesign on 200,000 generated lines; writes `Task07/q7_comparison.csv` and `Task07/statement_200000.txt`. |

## Evidence

Screenshots supplied from the student's Windows 10 / Python 3.11.6 runs are saved in each task's `evidence/` folder. The keyboard-checker image was excluded because it is unrelated to the assignment.

- Q1 includes the eight boundary cases and comparison of the two decision structures.
- Q2 includes the while-loop and recursive demonstration. The supplied for-loop capture shows the beginning of that section; the full output can be reproduced by running the command above.
- Q3 includes normalised valid/invalid registrations and receipt formatting.
- Q4 includes three-run averages and its StringIO/file alternatives. Raw readings are in `Task04/timings.csv`.
- Q5 includes the mutable-default bug, corrected independent orders and scope demonstrations.
- Q6 includes answers for n=1 to 6, call counts through n=30 and the memoised recursion limit at n=1,000. The iterative n=1,000 output is produced after the error message; run the program and scroll to the end to see the final line.
- Q7 includes three original/streaming timing runs, average time, record count, file size and exact-output validation. Raw readings are in `Task07/q7_comparison.csv`.

## Measured results

### Q4 – String building (average of three runs)

| Lines | `+=` (s) | `join()` (s) | f-string builder (s) |
|---:|---:|---:|---:|
| 1,000 | 0.000364 | 0.000023 | 0.000203 |
| 10,000 | 0.003862 | 0.000368 | 0.002280 |
| 200,000 | 0.691578 | 0.007892 | 0.054115 |

The three methods produced identical text (3,048,890 characters) in the measured run.

### Q7 – Original versus streaming redesign (200,000 lines)

| Measure | Original `+=` | Streaming |
|---|---:|---:|
| Run 1 (s) | 0.603374 | 0.138529 |
| Run 2 (s) | 0.686755 | 0.144824 |
| Run 3 (s) | 0.485828 | 0.151262 |
| Average (s) | 0.591986 | 0.144871 |

The average streaming time was about 4.09 times faster in this run. Both versions produced matching statement text. Timings are specific to the recorded Windows 10 / Python 3.11.6 run.

## GitHub commit history

The assignment folders were committed and pushed separately. The final terminal verification on 15 November 2026 showed the seven task commits (Task01–Task07), the initial README/setup commit, branch `main` tracking `origin/main`, and a clean working tree.

## Final submission checklist

- [x] Repository name: `CSA08-192365059-Assignment2`.
- [x] README includes student name, register number, Python version, run commands and result notes.
- [x] `requirements.txt` is present; no third-party packages are required.
- [x] Task01–Task07 source files and evidence folders are uploaded.
- [x] Q4 and Q7 raw CSV timing data are included.
- [x] At least one separate commit per task is pushed to GitHub.
- [x] GitHub repository is public.
- [x] Final report includes the GitHub repository URL.

**Submission repository URL:** https://github.com/Karthikdj2028/CSA08-192365059-Assignment2

## Important assumptions

- Q1 does not state monetary amounts for subsidies. The program reports eligibility categories only.
- Q2 uses sample OTP values so the two loop designs can be executed repeatedly; the sample expected OTP is `482916`.
- Q5 uses 5% GST only as an example to demonstrate returning multiple values; the assignment does not specify a GST rate.
- Q7 selects Q4's long-statement problem as the redesign target. The revised program streams generated lines to a file rather than retaining one complete large string in memory.
