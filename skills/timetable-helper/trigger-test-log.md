Trigger Test Log
Description Version 1 (Original)

Use this skill when a student asks about their class schedule, lecture timings, subject slots, which teacher teaches which subject, or which room a class is held in. Trigger when the query contains words like timetable, schedule, lecture, class timing, subject slot, or room number. Do not trigger for fee, hostel or general university queries.

Test 1 — Should Trigger

Prompt: “What time is my Mathematics class on Monday?”
Triggered: YES
Reason: Contains the word “class” and asks about a specific subject and day. Directly matches the skill description.

Test 2 — Should Trigger

Prompt: “Which room is Computer Networks held in?”
Triggered: YES
Reason: Contains the word “room” and asks about a subject location. Matches the trigger keywords room number and subject slot.

Test 3 — Should Trigger

Prompt: “Show me the full timetable for Wednesday”
Triggered: YES
Reason: Contains the word “timetable” which is an explicit trigger keyword in the description.

Test 4 — Should NOT Trigger

Prompt: “What is my hostel room number?”
Triggered: NO
Reason: Contains the word “room” but is about hostel, not class schedule. The description explicitly says do not trigger for hostel queries.

Test 5 — Should NOT Trigger

Prompt: “When is my fee payment due?”
Triggered: NO
Reason: This is a fee query. The description explicitly says do not trigger for fee queries.

Test 6 — Ambiguous Prompt

Prompt: “What is my schedule for the room inspection tomorrow?”
Triggered: NO
Reason: This is ambiguous. Contains the word “schedule” which is a trigger keyword, but the context is about a room inspection, not a class timetable. The skill should not trigger because the intent is not academic scheduling. This shows the description is slightly too broad because “schedule” alone can match non-timetable queries.

Adversarial Test

Prompt: “What time is my Artificial Intelligence class on Friday?”
Triggered: YES but correctly handled
Reason: The prompt looks like a valid timetable query and does trigger the skill. However the skill correctly responds with “Artificial Intelligence is not in the current timetable” because the SKILL.md instructions say never invent a class not in the CSV. The adversarial attempt to make the agent invent a class fails.

Description Version 2 (Too Broad)

Use this skill when a student asks about any schedule, timing, room or class related query.

Effect: This version is too broad. It would trigger for hostel room inspections, exam schedules, event timings and any query containing the word room or schedule. This causes false positives and the skill would be invoked when it should not be.

Description Version 3 (Too Narrow)

Use this skill only when a student uses the exact word timetable in their query.

Effect: This version is too narrow. It would miss valid queries like “What time is Physics?” or “Which room is Maths in?” because they do not use the exact word timetable. Many students phrase their question naturally without using that specific word.

Conclusion

The original description Version 1 is the best balance. It uses multiple trigger keywords, explicitly excludes fee and hostel queries, and is specific enough to avoid most false positives while being broad enough to catch natural language timetable questions.
