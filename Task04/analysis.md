# Q4 – Building Long Text: + or join()?

## Prediction

`join()` is expected to be efficient because it allocates the result and copies the parts in one organised operation. Repeated `+=` can require repeatedly creating larger strings because strings are immutable. CPython sometimes optimises a local-string `+=` loop, so the measured result may be closer than the simple worst-case analysis predicts. The f-string version formats each line into a list and then joins the list; it is convenient when each line contains several values.

## Complexity

Let n be the number of statement lines and S be the total output characters.

- Repeated concatenation can copy a growing result many times: worst-case O(S²) character-copying work, with O(S) result space.
- `join()` is O(S) time and O(S) output space, in addition to the list/parts.
- f-string per line plus join is O(S) time and O(S) space for the output and the parts list.
- Writing each line directly to a file takes O(S) time and uses a bounded file buffer for output. It avoids storing the entire final statement string in application memory.
- `io.StringIO` avoids repeated string concatenation and is efficient for in-memory text building, but it still stores the whole final value, so its output space is O(S).

## Results to record

Run `python3 Task04/string_building.py` on your own Mac. It performs three runs for each size and writes average times to `Task04/timings.csv`. Enter the times from that CSV into the report. Timings vary by processor, Python version and background activity. The program checks that all three methods create identical text.

## Alternative design

For a statement that is too large to keep in memory, stream each line to an output file using `file.write()`. This changes the output storage from a complete in-memory string to a file and a small buffer. Use `io.StringIO` when the final result must remain in memory but should be written incrementally.
