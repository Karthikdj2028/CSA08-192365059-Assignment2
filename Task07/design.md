# Q7 – Day-4 Design Challenge: Diagnose, Redesign and Validate

## Selected program: Q4 monthly statement generation

The original statement builder repeatedly concatenates a growing string using `+=`. The amount of statement text grows with the number of calls and SMS records. Because strings are immutable, each concatenation may create a new string and copy existing characters. The timing results from Q4 provide the evidence for the chosen bottleneck; the exact measurements must be filled in from the Mac run.

## A. Diagnose the bottleneck

The repeated concatenation happens once per statement line. As the line count grows from 1,000 to 10,000 to 200,000, the amount of output data grows. The plus-builder holds the full statement in memory. In the worst case, repeatedly copying the growing string can approach O(S^2) character-copying work, where S is the final number of characters. CPython may optimise some `+=` cases, so diagnosis must use the actual timings instead of assuming that every run has the theoretical worst-case speed.

## B. Design objective

For 200,000 statement lines, generate exactly the same statement text while avoiding a complete in-memory output string during statement generation. Compare average generation time and confirm identical output. Also report the final file size and output line/record count.

## C. Revised solution

The original function builds one string in memory. The revised function generates one line at a time and writes it directly to a buffered output file. It uses no list of all lines and no complete statement string during the writing step. The operating system/Python file buffer handles small writes. Extra application space is O(1) for each generated line (apart from the fixed file buffer), while disk space is O(S). The input data is generated in the loop, not pre-stored in a list.

Pseudocode:

```text
START
OPEN statement file for writing
FOR each record number from 0 to count - 1
    BUILD one formatted line
    WRITE the line to the file
    WRITE the separator
ENDFOR
CLOSE the file
END
```

Exact-content validation reads the generated file and compares it with the original output after both timed generation sections. That one-off validation temporarily loads the file into memory; it is not part of the redesigned production write step. For a real large deployment, a streaming checksum or record-by-record comparison could validate without loading the whole file.

## D. Prediction before implementation

The prediction is that streaming will use less additional memory during generation because it does not create a complete result string. Runtime may be faster or slower than `+=` depending on Python's string-concatenation optimisation and disk speed. Therefore, the main measurable objective is bounded output memory with exact text, not a guaranteed speed increase.

## E. Implementation and validation

Run `python3 Task07/streaming_redesign.py`. It runs each version three times with the same count (200,000), reports the individual and average times, validates exact text equality, reports output file size and separator count, and saves raw measurements to `Task07/q7_comparison.csv`.

Copy your actual Mac values into the report. Do not use timings from another computer.

## F. Final defence and trade-offs

The redesign achieves the memory objective if it writes the complete output without constructing one large Python string. If the file matches exactly, correctness is preserved. Streaming needs disk space, file error handling and later file reading if the caller needs the whole statement as a string. The original `+=` method may remain suitable for very small statements. `join()` is a good choice when all parts and the final string fit comfortably in memory; streaming is more suitable when the statement is large or the consumer can read a file.
