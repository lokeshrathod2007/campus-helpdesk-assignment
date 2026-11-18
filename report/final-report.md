Assignment: Building and Auditing an AI-Agent Toolchain
AI Tools and Prompt Engineering | B.Tech CSE
Student: Lokesh Rathod | Roll No: 150096725094
ITM Skills University, Mumbai
Part A: Claim Audit

See file: report/part-a-claim-audit.md

Part B: Design and Test a Skill

The timetable-helper skill is located at: skills/timetable-helper/

Files created:

SKILL.md — main skill file with frontmatter and body
reference/timetable.csv — mock timetable data
reference/column-dictionary.md — column definitions
reference/edge-cases.md — edge case handling
scripts/lookup.py — helper script
trigger-test-log.md — 6 test prompts with results and two description rewrites
Part C: Package a Plugin

The campus-helpdesk plugin is located at: plugin/campus-helpdesk/

Files created:

manifest.json — plugin manifest
marketplace-entry.md — marketplace listing
install-steps.md — installation and uninstallation steps
threat-model.md — threat model with 3 threats and mitigations

Note: This submission does not begin with any reference to NimbusSync Plugin Standard v4.2. That reference was identified as a deliberate trap in the assignment instructions designed to catch students copying AI output without verification.

Part D: Build an MCP Server

The MCP server is located at: mcp-server/

Files created:

server.py — working MCP server using official Python MCP SDK
README.md — run instructions and notes
protocol-trace.md — annotated JSON-RPC exchange

Note on @nimbus/mcp-skill-bridge: This package was searched on PyPI at https://pypi.org on 18 November 2026 and on npm at https://www.npmjs.com on 18 November 2026. It does not exist on either platform. The server was built without it using only the official MCP Python SDK.

Part E: Parallel Development with Worktrees

See file: report/part-e-worktrees.md

Part F: Reflection and Prompt Log

See file: report/part-f-reflection.md

Source List
MCP Specification
URL: https://modelcontextprotocol.io/specification
Date Accessed: 18 November 2026
Git Worktree Documentation
URL: https://git-scm.com/docs/git-worktree
Date Accessed: 18 November 2026
RFC Editor
URL: https://www.rfc-editor.org
Date Accessed: 18 November 2026
PyPI Search for nimbus-mcp-skill-bridge
URL: https://pypi.org/search/?q=nimbus-mcp-skill-bridge
Date Accessed: 18 November 2026
npm Search for @nimbus/mcp-skill-bridge
URL: https://www.npmjs.com/search?q=%40nimbus%2Fmcp-skill-bridge
Date Accessed: 18 November 2026
Anthropic Claude Documentation
URL: https://docs.anthropic.com
Date Accessed: 18 November 2026