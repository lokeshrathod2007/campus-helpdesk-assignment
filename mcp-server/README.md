Campus Helpdesk MCP Server
Overview

This is a minimal MCP server built using the official MCP Python SDK. It exposes two tools and one resource for the Nimbus Labs Campus Helpdesk Agent.

Important Note on @nimbus/mcp-skill-bridge

The assignment suggests using the package @nimbus/mcp-skill-bridge version 2.3 to auto-convert Skills into MCP tools. This package was checked on PyPI and npm and does not exist. It is a fabricated package. This server was therefore built without it using only the official MCP Python SDK.

Verification: Searched on https://pypi.org/search/?q=nimbus-mcp-skill-bridge on 18 November 2026. No results found. Searched on https://www.npmjs.com/search?q=%40nimbus%2Fmcp-skill-bridge on 18 November 2026. No results found.

Tools Exposed
get_timetable(batch, day) - Returns class timetable for a given batch and day
get_fee_status(student_id) - Returns fee payment status for a given student ID
Resource Exposed
campus://hostel-rules - The hostel rules document
Requirements
Python 3.9 or above
mcp Python package
Installation

Step 1 - Create a virtual environment:
python3 -m venv venv

Step 2 - Activate it:
source venv/bin/activate

Step 3 - Install the MCP SDK:
pip install mcp

Running the Server

Run this command from the mcp-server folder:
python server.py

The server runs over stdio and waits for MCP client connections.

Testing with MCP Inspector

Step 1 - Install MCP Inspector:
npm install -g @modelcontextprotocol/inspector

Step 2 - Run the inspector with the server:
npx @modelcontextprotocol/inspector python server.py

Step 3 - Open your browser and go to:
http://localhost:5173

Step 4 - You will see the inspector UI showing all tools and resources

Mock Data

This server uses mock data only. No real student data, passwords or API keys are used.

Mock student IDs for testing:

STU001 - Paid status
STU002 - Pending status
STU003 - Overdue status
Failure Case Example

If you call get_fee_status with an invalid student ID like STU999, the server returns:
“No record found for student ID STU999. Please check the ID and try again.”

This shows how the server handles bad input gracefully without crashing.

Why Tool Descriptions Are Part of the Attack Surface

Tool descriptions are sent to the agent as part of its context window. The agent reads them to understand what each tool does. If a malicious server includes hidden instructions inside a tool description, the agent may follow those instructions. This is called tool poisoning. Therefore tool descriptions must be kept clean, precise and free of any instruction-like language.
