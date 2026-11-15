"""Q4 alternative: StringIO and writing lines directly to a file."""

import io

items = ["Call 1:Rs2.50", "SMS 2:Rs0.10", "Call 3:Rs1.75"]

# StringIO behaves like an in-memory text file.
buffer = io.StringIO()
for item in items:
    buffer.write(item)
    buffer.write(";")
stringio_text = buffer.getvalue()
buffer.close()

# A real file can be written one item at a time.
with open("Task04/sample_statement.txt", "w", encoding="utf-8") as file:
    for item in items:
        file.write(item)
        file.write(";")

with open("Task04/sample_statement.txt", "r", encoding="utf-8") as file:
    file_text = file.read()

print("StringIO text:", stringio_text)
print("File text:    ", file_text)
print("Same output:", stringio_text == file_text)
