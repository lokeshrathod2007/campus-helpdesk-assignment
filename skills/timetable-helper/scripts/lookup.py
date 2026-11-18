import csv
import sys

def lookup_timetable(query_day=None, query_subject=None):
results = []
with open(“reference/timetable.csv”, “r”) as f:
reader = csv.DictReader(f)
for row in reader:
day_match = True
subject_match = True
if query_day:
day_match = row[“day”].lower() == query_day.lower()
if query_subject:
subject_match = row[“subject”].lower() == query_subject.lower()
if day_match and subject_match:
results.append(row)
return results

def main():
if len(sys.argv) < 2:
print(“Usage: python lookup.py <day> or python lookup.py <subject>“)
return
query = sys.argv[1]
days = [“monday”, “tuesday”, “wednesday”, “thursday”, “friday”]
if query.lower() in days:
results = lookup_timetable(query_day=query)
else:
results = lookup_timetable(query_subject=query)
if not results:
print(“Not found in timetable.”)
else:
for row in results:
print(row[“day”], row[“time”], row[“subject”], row[“teacher”], row[“room”])

main()
