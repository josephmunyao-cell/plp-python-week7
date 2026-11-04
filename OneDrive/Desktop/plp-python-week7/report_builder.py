import csv

try:
    with open("hubs.csv", "r") as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    # Print "hubs.csv not found" and set rows to an empty list
    print("hubs.csv not found")
    rows = []

total = 0
passed = 0

for row in rows:
    # Convert row["score"] to a whole number and store it in score
    score = int(row["score"])
    total += score
    if score >= 50:
        # Add 1 to passed
        passed += 1

# Calculate failed learners count
failed = len(rows) - passed

average = round(total / len(rows), 1) if len(rows) > 0 else 0

with open("report.txt", "w") as f:
    f.write("LEARNER REPORT\n")
    f.write("Total learners: " + str(len(rows)) + "\n")
    f.write("Passed: " + str(passed) + "\n")
    # Write the failed count the same way
    f.write("Failed: " + str(failed) + "\n")
    f.write("Average score: " + str(average) + "\n")

print("Report written to report.txt")