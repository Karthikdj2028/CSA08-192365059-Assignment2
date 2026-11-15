# CSA08-192365059-Assignment2

**Assignment:** Assignment 2 – Control Flow, Strings and Functions  
**Course:** CSA08 – Python Programming  
**Student:** Karthikeyan S  
**Register Number:** 192365059D (confirm the exact format shown in your portal before final submission)  
**Nature:** Individual  
**Platform:** macOS  
**Python command:** `python3`  
**Python version:** Run `python3 --version` and record the exact result.

**GitHub repository:** https://github.com/Karthikdj2028/CSA08-192365059-Assignment2

## Project overview

This project covers the seven questions in Assignment 2 using beginner-friendly Python. The main concepts are `if`, `if-else`, `if-elif-else`, `while`, `for`, `break`, `continue`, `pass`, loop `else`, string methods and slicing, functions, parameters, scope, recursion, memoisation and performance measurement.

| Folder | Assignment question | Main work |
|---|---|---|
| Task01 | Q1 – Decisions with Many Boundaries | Separate `if` versus `if-elif-else`, boundaries, `match-case`, lookup list |
| Task02 | Q2 – Loops that Count Attempts | `while`, `for`, blank OTP handling, loop `else`, recursion alternative |
| Task03 | Q3 – Vehicle Registration Validator | Normalising, validating and formatting strings without regular expressions |
| Task04 | Q4 – Building Long Text | `+=`, `join()`, f-strings, measurements at 1,000 / 10,000 / 200,000 lines |
| Task05 | Q5 – Functions, Parameters and Scope | Mutable default argument bug, corrected list handling, GST, local/global/nonlocal |
| Task06 | Q6 – Recursion and Its Limits | Naive recursion, memoisation, function-call counts, recursion limit, loop solution |
| Task07 | Q7 – Diagnose, Redesign and Validate | Streaming a large statement to a file and comparing it with the original builder |

Each folder contains Python files, a short task README and an `evidence/` folder. Save your own screenshots and raw timing files there after running on your Mac.

## Python and libraries

- Python 3.10 or later is required for the `match-case` alternative in Task01. Python 3.13.15 was used for the prepared example code; enter the version actually installed on your Mac.
- Third-party packages: none.
- Standard-library modules: `time`, `io`, `sys`, `functools`, `csv`, `os`, and `tempfile`.
- `requirements.txt` is included. No `pip install` command is needed.

## Setup on Mac

Open this folder in VS Code. Select **Terminal → New Terminal**. Ensure the terminal is at the project root (the folder containing this README).

```bash
python3 --version
pwd
```

Optional virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 --version
```

## Run commands

Run these from the project root. For interactive tasks, the sample scripts are deterministic demonstrations; you can also call their functions with your own test data.

| Task | Command | What to check |
|---|---|---|
| Task01 | `python3 Task01/decisions.py` | Eight households, including 100 / 101 / 200 / 201 unit boundaries; compare separate `if` and `if-elif-else`. |
| Task02 | `python3 Task02/otp_loops.py` | While loop and for loop; blank entries do not consume attempts; loop `else` locks after three wrong attempts. |
| Task03 | `python3 Task03/plate_validator.py` | Complete the Code functions, six predictions, valid/invalid results and receipt formatting. |
| Task04 | `python3 Task04/string_building.py` | `+=`, `join()` and f-string builders; three-run average at 1,000 / 10,000 / 200,000 lines; CSV results. |
| Task05 | `python3 Task05/orders_and_scope.py` | Mutable default bug, fixed orders for three customers, defaults tuple and scope examples. |
| Task06 | `python3 Task06/stair_ways.py` | Answers 1–6, call counts for 10 / 20 / 25 / 30, recursion-limit demonstration and iterative n=1,000 result. |
| Task07 | `python3 Task07/streaming_redesign.py` | Original versus streaming redesign using the same 200,000 generated lines; time, output validation and file-size evidence. |

Additional Task04 alternative implementations:

```bash
python3 Task04/string_alternatives.py
```

## Evidence instructions

1. Run each command on your Mac.
2. Capture the full terminal output with **Shift + Command + 4**.
3. Save screenshots inside that task's `evidence/` directory.
4. Task04 and Task07 also generate CSV files containing raw benchmark results. Keep those files with the task evidence.
5. Do not copy example timings from another computer. Record your own averages in the report.
6. For Q1, keep the prediction table in the report before the observed output.
7. For Q6 and Q7, include call counts / timing tables; a screenshot alone is not enough.

## GitHub commit workflow

Create a public repository named `CSA08-192365059-Assignment2` (or use Private and add the faculty as a collaborator). For each task, run the program, save evidence, then commit the task separately.

Example:

```bash
git add Task01
git commit -m "feat(task01): analyse subsidy decision boundaries"
git push origin main
```

Use one task folder per commit for Task02 through Task07. Avoid a single final bulk upload. Do not use `git push --force`.

## Before submission

- [ ] Confirm register-number format against the portal (the portal displays `192365059D`).
- [ ] Record the exact `python3 --version` output.
- [ ] Execute all seven task programs on your Mac.
- [ ] Replace timing placeholders in the report using your own CSV/output results.
- [ ] Save evidence screenshots in all task folders.
- [ ] Commit each task separately and push it to GitHub.
- [ ] Add the working GitHub URL to the report cover page and portal.
- [ ] Check `git status` and `git log --oneline`.

## Important assumptions

- Q1 does not state the monetary amount of each subsidy. The program therefore reports the eligibility category only and does not invent a rupee amount.
- Q2 uses sample OTP values in a list so both loop versions can be executed and compared repeatedly. The sample expected OTP is `482916`.
- Q5 uses an illustrative GST rate of 5% only to demonstrate returning both total and GST; replace it only if your instructor specifies a different rate.
- Q7 uses Q4's long-statement problem as the redesign target. The revised version streams generated lines to a file, reducing the need to hold the complete statement string in memory.
