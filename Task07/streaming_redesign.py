"""Q7: Redesign large statement building to stream directly to a file."""

import csv
import os
import time


COUNT = 200_000
OUTPUT_FILE = "Task07/statement_200000.txt"


def build_original_plus(count):
    """Original design: keep appending to one growing string."""
    text = ""
    for i in range(count):
        line = f"Item{i}:Rs{i % 50}"
        text += line + ";"
    return text


def write_streaming(count, path):
    """Revised design: write each generated statement line to a buffered file."""
    with open(path, "w", encoding="utf-8") as file:
        for i in range(count):
            line = f"Item{i}:Rs{i % 50}"
            file.write(line)
            file.write(";")


def validate_file(path, expected_text):
    """Read the file back once and compare exact text during validation."""
    with open(path, "r", encoding="utf-8") as file:
        actual_text = file.read()
    return actual_text == expected_text


print("Q7 - ORIGINAL VERSUS STREAMING REDESIGN")
print("Number of statement lines:", COUNT)

original_times = []
original_text = ""
for run in range(3):
    start = time.perf_counter()
    original_text = build_original_plus(COUNT)
    original_times.append(time.perf_counter() - start)

stream_times = []
for run in range(3):
    start = time.perf_counter()
    write_streaming(COUNT, OUTPUT_FILE)
    stream_times.append(time.perf_counter() - start)

original_average = sum(original_times) / len(original_times)
stream_average = sum(stream_times) / len(stream_times)

same_text = validate_file(OUTPUT_FILE, original_text)
file_size = os.path.getsize(OUTPUT_FILE)

print("Original += times:", [round(value, 6) for value in original_times])
print("Streaming times:", [round(value, 6) for value in stream_times])
print(f"Original average: {original_average:.6f} s")
print(f"Streaming average: {stream_average:.6f} s")
print("Exact output match:", same_text)
print("Output file size:", file_size, "bytes")
print("Original in-memory string size:", len(original_text), "characters")
print("Semicolon count:", original_text.count(";"))

with open("Task07/q7_comparison.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["run", "original_plus_seconds", "streaming_seconds"])
    for index in range(3):
        writer.writerow([index + 1, original_times[index], stream_times[index]])
    writer.writerow(["average", original_average, stream_average])

print("Raw measurements saved to Task07/q7_comparison.csv")
print("Generated statement saved to", OUTPUT_FILE)
