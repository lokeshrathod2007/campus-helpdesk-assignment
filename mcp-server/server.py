import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

app = Server(“campus-helpdesk-server”)

TIMETABLE = {
“Monday”: [
{“time”: “09:00-10:00”, “subject”: “Mathematics”, “teacher”: “Prof. Sharma”, “room”: “A101”},
{“time”: “10:00-11:00”, “subject”: “Physics”, “teacher”: “Prof. Mehta”, “room”: “A102”},
{“time”: “11:00-12:00”, “subject”: “English”, “teacher”: “Prof. Kulkarni”, “room”: “B201”},
{“time”: “14:00-15:00”, “subject”: “Computer Networks”, “teacher”: “Prof. Joshi”, “room”: “Lab1”}
],
“Tuesday”: [
{“time”: “09:00-10:00”, “subject”: “Data Structures”, “teacher”: “Prof. Sharma”, “room”: “A101”},
{“time”: “10:00-11:00”, “subject”: “Mathematics”, “teacher”: “Prof. Mehta”, “room”: “A102”},
{“time”: “11:00-12:00”, “subject”: “Computer Networks”, “teacher”: “Prof. Joshi”, “room”: “Lab1”},
{“time”: “14:00-15:00”, “subject”: “Physics”, “teacher”: “Prof. Kulkarni”, “room”: “A103”}
]
}

FEE_DATA = {
“STU001”: {“name”: “Mock Student A”, “status”: “Paid”, “amount”: 50000, “due_date”: “2026-12-01”},
“STU002”: {“name”: “Mock Student B”, “status”: “Pending”, “amount”: 50000, “due_date”: “2026-12-01”},
“STU003”: {“name”: “Mock Student C”, “status”: “Overdue”, “amount”: 50000, “due_date”: “2026-11-01”}
}

HOSTEL_RULES = “””

Hostel Rules - Nimbus University
Gate closing time is 10:00 PM on weekdays and 11:00 PM on weekends.
Guests are allowed only between 9:00 AM and 6:00 PM.
Cooking in rooms is strictly prohibited.
Ragging in any form will result in immediate expulsion.
Students must carry their ID cards at all times.
Noise must be kept to a minimum after 10:00 PM.
Common areas must be kept clean at all times.
Any damage to hostel property will be charged to the student.
“””

@app.list_tools()
async def list_tools():
return [
types.Tool(
name="get_timetable",
description="Returns the class timetable for a given batch and day. Use this when a student asks about their class schedule.",
inputSchema={
“type”: “object”,
“properties”: {
“batch”: {
“type”: “string”,
“description”: “The student batch name, for example CSE-2025”
},
“day”: {
“type”: “string”,
“description”: “The day of the week, for example Monday or Tuesday”
}
},
“required”: [“batch”, “day”]
}
),
types.Tool(
name="get_fee_status",
description="Returns the fee payment status for a given student ID. Use this when a student asks about their fee.",
inputSchema={
“type”: “object”,
“properties”: {
“student_id”: {
“type”: “string”,
“description”: “The student ID, for example STU001”
}
},
“required”: [“student_id”]
}
)
]

@app.call_tool()
async def call_tool(name: str, arguments: dict):
if name == “get_timetable”:
day = arguments.get(“day”, “”)
if day not in TIMETABLE:
return [types.TextContent(type="text", text=f"No timetable found for {day}. Available days are Monday and Tuesday.")]
classes = TIMETABLE[day]
result = f"Timetable for {day}:\n"
for c in classes:
result += f”- {c[‘time’]}: {c[‘subject’]} with {c[‘teacher’]} in room {c[‘room’]}\n”
return [types.TextContent(type="text", text=result)]

elif name == "get_fee_status":
    student_id = arguments.get("student_id", "")
    if student_id not in FEE_DATA:
        return [types.TextContent(type="text", text=f"No record found for student ID {student_id}. Please check the ID and try again.")]
    fee = FEE_DATA[student_id]
    result = f"Fee Status for {fee['name']} ({student_id}):\nStatus: {fee['status']}\nAmount: Rs. {fee['amount']}\nDue Date: {fee['due_date']}"
    return [types.TextContent(type="text", text=result)]

else:
    return [types.TextContent(type="text", text=f"Unknown tool: {name}")]

@app.list_resources()
async def list_resources():
return [
types.Resource(
uri="campus://hostel-rules",
name="Hostel Rules",
description="The official hostel rules document for Nimbus University",
mimeType="text/plain"
)
]

@app.read_resource()
async def read_resource(uri: str):
if uri == “campus://hostel-rules”:
return HOSTEL_RULES
raise ValueError(f"Unknown resource: {uri}")

async def main():
async with stdio_server() as (read_stream, write_stream):
await app.run(read_stream, write_stream, app.create_initialization_options())

if name == “main”:
asyncio.run(main())
