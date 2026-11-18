name: timetable-helper
description: Use this skill when a student asks about their class schedule, lecture timings, subject slots, which teacher teaches which subject, or which room a class is held in. Trigger when the query contains words like timetable, schedule, lecture, class timing, subject slot, or room number. Do not trigger for fee, hostel or general university queries.
Timetable Helper Skill

This skill teaches the agent how to answer student timetable queries using a CSV file containing the class schedule data.

What This Skill Does

It allows the agent to look up:

Which classes are scheduled on a given day
What time a specific subject is held
Which teacher is assigned to a subject
Which room a class takes place in

How To Use It
The timetable data is stored in reference/timetable.csv
When a student asks a timetable question, read the CSV and find the matching row
Return the day, time, subject, teacher and room in a clear sentence
If the subject or day is not found in the CSV, say “This subject is not in the current timetable” — do not invent classes

Important Rules
Never invent a class, subject, teacher or room that is not in the CSV
If asked about a subject not in the CSV, respond with “Not found in timetable”
Do not answer fee or hostel queries using this skill
See reference/column-dictionary.md for column definitions
See reference/edge-cases.md for handling ambiguous queries