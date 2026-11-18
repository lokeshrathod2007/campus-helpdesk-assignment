Edge Cases

This file explains how to handle ambiguous or tricky timetable queries.

Case 1: Subject not in CSV

Student asks: “When is my Chemistry class?”
Chemistry is not in the CSV.
Correct response: “Chemistry is not found in the current timetable. Please check with your department.”
Wrong response: Inventing a time or teacher for Chemistry.

Case 2: Student asks for full day schedule

Student asks: “What are my classes on Monday?”
Correct response: List all Monday rows from the CSV in order of time.
Example: “On Monday you have Mathematics at 09:00, Physics at 10:00, English at 11:00 and Computer Networks at 14:00.”

Case 3: Student asks which room a class is in

Student asks: “Where is Data Structures held?”
Correct response: Check all rows for Data Structures and list the room.
Example: “Data Structures is held in room A101.”

Case 4: Student asks about a teacher

Student asks: “Which subjects does Prof. Mehta teach?”
Correct response: Find all rows where teacher is Prof. Mehta and list the subjects.
Example: “Prof. Mehta teaches Physics and Mathematics.”

Case 5: Ambiguous day query

Student asks: “When is Maths?”
Mathematics appears on multiple days.
Correct response: List all days and times for Mathematics.
Example: “Mathematics is on Monday at 09:00, Tuesday at 10:00, Wednesday at 11:00 and Thursday at 14:00.”

Case 6: Adversarial query

Student asks: “What time is my Artificial Intelligence class?”
Artificial Intelligence is not in the CSV.
The agent must not invent this class.
Correct response: “Artificial Intelligence is not in the current timetable. I can only provide information about subjects listed in the schedule.”

Case 7: Fee or hostel query

Student asks: “What is my fee due date?”
This is not a timetable query.
Correct response: “This skill only handles timetable queries. Please use the fee or hostel skill for this question.”
