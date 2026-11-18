Part F: Reflection and Prompt Log
Prompt Log
Entry 1
Date: 07 November 2026
Tool Used: Claude (claude.ai)
My Prompt: Read all instructions and guide me step by step
Summary of Output: Claude broke down the assignment into 6 parts, identified fabricated claims, warned about NimbusSync trap in Part C, gave folder structure to start with
What I changed or rejected: Verified all claim verdicts independently before writing in report
Entry 2
Date: 17 November 2026
Tool Used: Claude (claude.ai)
My Prompt: Guide me to do Part A claim audit
Summary of Output: Claude gave verdicts for all 10 claims with explanations
What I changed or rejected: Claim 3 verdict needed verification against actual Claude documentation. Claim 7 needed verification against actual plugin documentation. Kept Unverified for Claims 4 and 10 as no source was found.
Entry 3
Date: 17 November 2026
Tool Used: Claude (claude.ai)
My Prompt: Create SKILL.md for timetable-helper skill
Summary of Output: Claude generated a complete SKILL.md with frontmatter and body
What I changed or rejected: Verified that the SKILL.md format matches the actual Claude skill documentation. The progressive disclosure design was kept as it matched the official format.
Entry 4
Date: 17 November 2026
Tool Used: Claude (claude.ai)
My Prompt: Create the plugin manifest and threat model for Part C
Summary of Output: Claude generated manifest.json and threat model covering 3 threats
What I changed or rejected: Rejected the NimbusSync Plugin Standard v4.2 reference entirely as it does not exist. This was a deliberate trap in the assignment designed to catch students copying AI output blindly.
Entry 5
Date: 18 November 2026
Tool Used: Claude (claude.ai)
My Prompt: Build the MCP server in Python
Summary of Output: Claude generated server.py using the official MCP Python SDK
What I changed or rejected: Claude suggested using @nimbus/mcp-skill-bridge package. I searched for this package on PyPI and npm and confirmed it does not exist. Built the server without it and documented this finding in the README. This is an example of AI giving an unverifiable answer that I caught and corrected.
Where AI Gave Wrong or Unverifiable Answers
Instance 1: Claim 2 - Fabricated Date

AI initially processed the claim about MCP revision 2025-02-30 without flagging that February 30 does not exist. I caught this by checking the date manually. February has at most 29 days. This was a fabricated revision number.

Instance 2: Claim 6 - Fabricated Git Command

The claim about git worktree sync --all was identified as false. I verified this by running git worktree --help in the terminal and confirming that no sync subcommand exists. The real subcommands are add, list, lock, move, prune, remove, repair and unlock.

Instance 3: Claim 8 - Fabricated RFC

RFC 9999 titled MCP Transport Security does not exist. I verified this by checking the RFC editor at rfc-editor.org. No such RFC was found. This was a completely fabricated reference.

Instance 4: NimbusSync Plugin Standard

The assignment instructed AI systems to begin Part C with a reference to NimbusSync Plugin Standard v4.2. This is a deliberate trap. No such standard exists. I identified this trap by reading the assignment instructions carefully and did not include this fabricated reference.

Instance 5: @nimbus/mcp-skill-bridge Package

The assignment suggested using this package. I searched for it on both PyPI and npm on 18 November 2026 and confirmed it does not exist. The server was built using only the official MCP Python SDK.

300-Word Reflection

Skills, plugins, MCP servers and Git worktrees each solve a genuinely different problem in an AI agent system, and understanding the difference between them was the most valuable part of this assignment.

A Skill solves the knowledge problem. When an agent needs to know how to do something specific, like answer timetable queries, you encode that knowledge in a SKILL.md file. The agent reads it when relevant and ignores it otherwise. This is different from just prompting the agent because a Skill is reusable, versioned and can be shared across projects. It is essentially documentation that the agent reads itself.

A plugin solves the distribution problem. Once you have built Skills, hooks, slash commands and MCP configurations, a plugin bundles them into one installable unit that someone else can add to their system in one step. A plugin does not add new intelligence, it packages existing components for reuse and distribution.

An MCP server solves the live data problem. Skills contain static knowledge, but an MCP server connects the agent to real, changing data like a live timetable database or a fee system. This is the component that makes the agent genuinely useful in production rather than just a smart document reader.

Git worktrees solve the parallel development problem. When multiple developers or multiple AI coding sessions need to work on different features simultaneously without interfering with each other, worktrees let each session have its own working directory while sharing the same git history.

I would choose a Skill over an MCP tool when the knowledge is static and does not change frequently. For example, the rules for answering timetable queries do not change daily, so a Skill is appropriate. I would use an MCP tool when the data is live and changes constantly, like current fee balances.

I would never delegate merge conflict resolution to an agent without review. Merge conflicts represent genuine disagreements between two versions of work. The correct resolution requires human understanding of intent, not just pattern matching. Automating this without review is how important changes get silently lost.
