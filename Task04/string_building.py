"""Q4: Compare +=, join(), and f-string statement construction."""

import csv
import time


def build_plus(parts):
    """Build a statement by repeatedly adding each item to a string."""
    text = ""
    for part in parts:
        text += part + ";"
    return text


def build_join(parts):
    """Build the same statement using one join operation."""
    return ";".join(parts) + ";"


def build_fstring(parts):
    """Build a formatted line for each item, then join the lines."""
    lines = []
    for part in parts:
        lines.append(f"{part};")
    return "".join(lines)


def average_time(builder, items, repeats=3):
    """Return the average time and final text from three runs."""
    total_time = 0.0
    result = ""
    for run in range(repeats):
        start = time.perf_counter()
        result = builder(items)
        total_time += time.perf_counter() - start
    return total_time / repeats, result


sizes = [1000, 10000, 200000]
rows = []
print("Q4 - STRING BUILDING BENCHMARK (average of 3 runs)")
print("LINES | += seconds | join seconds | f-string seconds | same text")

for count in sizes:
    items = [f"Item{i}:Rs{i % 50}" for i in range(count)]
    plus_time, plus_text = average_time(build_plus, items)
    join_time, join_text = average_time(build_join, items)
    f_time, f_text = average_time(build_fstring, items)
    same = plus_text == join_text == f_text
    print(f"{count:6} | {plus_time:10.6f} | {join_time:11.6f} | {f_time:15.6f} | {same}")
    rows.append([count, plus_time, join_time, f_time, len(join_text), same])

with open("Task04/timings.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["lines", "plus_average_seconds", "join_average_seconds", "fstring_average_seconds", "output_length", "same_text"])
    writer.writerows(rows)

print("\nRaw and average timings saved to Task04/timings.csv")
print("Expected output length for 200,000 lines: 3,048,890 characters.")
