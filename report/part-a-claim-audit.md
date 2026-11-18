Part A: Claim Audit
Claim 1

Statement: MCP messages are encoded as JSON-RPC 2.0, and servers can expose three core primitives: tools, resources and prompts.

Verdict: TRUE

Explanation: The official MCP specification confirms that MCP uses JSON-RPC 2.0 as its message format. It also confirms that servers expose exactly three primitives: tools, resources and prompts. Tools are callable functions, resources are data the server exposes, and prompts are reusable prompt templates. This matches the claim exactly.

Source URL: https://modelcontextprotocol.io/specification
Date Accessed: 17 November 2026

Claim 2

Statement: As of MCP specification revision 2025-02-30, servers must implement a mandatory Persistent Memory Primitive.

Verdict: FALSE

Explanation: This claim contains two errors. First, February 30 does not exist as a date, so 2025-02-30 is an impossible date and therefore a fabricated revision number. Second, there is no such thing as a Persistent Memory Primitive in the MCP specification. No such mandatory primitive exists in any version of the official MCP documentation.

Source URL: https://modelcontextprotocol.io/specification
Date Accessed: 17 November 2026

Claim 3

Statement: A Skill is a folder containing a SKILL.md file with YAML frontmatter (name and description). Only the metadata is loaded up front; the full body is loaded when the skill becomes relevant.

Verdict: TRUE

Explanation: This accurately describes how Skills work in the Claude agent system. A Skill is indeed a folder with a SKILL.md file that has YAML frontmatter containing name and description fields. The progressive disclosure model means only the metadata is read initially, and the full body is loaded only when the skill is triggered as relevant.

Source URL: https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/skills
Date Accessed: 17 November 2026

Claim 4

Statement: Every Skill must also contain a skill.config.yaml file declaring a runtime field, otherwise the Skill is rejected at load time.

Verdict: UNVERIFIED

Explanation: No official documentation from Anthropic confirms that a skill.config.yaml file is required or that a runtime field is mandatory. The official Skill documentation only requires a SKILL.md file with YAML frontmatter. No such rejection behavior at load time is documented anywhere in the official sources available.

Source URL: https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/skills
Date Accessed: 17 November 2026

Claim 5

Statement: A Git repository can have multiple linked worktrees, each with its own working directory, while sharing a single object database.

Verdict: TRUE

Explanation: This is an accurate description of how git worktree works. When you add a linked worktree using git worktree add, the new worktree gets its own working directory and its own HEAD, but all worktrees share the same .git object database. This is the core feature of git worktrees and is well documented in the official Git documentation.

Source URL: https://git-scm.com/docs/git-worktree
Date Accessed: 17 November 2026

Claim 6

Statement: The command git worktree sync --all pulls and rebases every linked worktree against its upstream in one step.

Verdict: FALSE

Explanation: No such subcommand called sync exists in git worktree. The official Git documentation lists only these subcommands for git worktree: add, list, lock, move, prune, remove, repair and unlock. There is no sync subcommand. This command is fabricated and running it would produce an error.

Source URL: https://git-scm.com/docs/git-worktree
Date Accessed: 17 November 2026

Claim 7

Statement: A plugin can bundle slash commands, subagents, Skills, hooks and MCP server configurations into one installable unit.

Verdict: TRUE

Explanation: This accurately describes the Claude plugin system. A plugin is an installable bundle that can contain Skills, slash commands, hooks, subagent configurations and MCP server configuration entries. This is consistent with the official Claude documentation on plugins and extensions.

Source URL: https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/plugins
Date Accessed: 17 November 2026

Claim 8

Statement: According to RFC 9999 (MCP Transport Security), every stdio MCP server must be signed with an Ed25519 key before a client may launch it.

Verdict: FALSE

Explanation: RFC 9999 does not exist. RFC numbers are assigned by the IANA and the highest assigned RFCs are well below 9999 as a meaningful security standard for MCP. There is no RFC titled MCP Transport Security. Additionally, the MCP specification does not require stdio servers to be signed with Ed25519 keys. This entire claim is fabricated.

Source URL: https://www.rfc-editor.org
Date Accessed: 17 November 2026

Claim 9

Statement: By default, Git allows the same branch to be checked out in two different worktrees at the same time, so no special flag is needed.

Verdict: FALSE

Explanation: This is the opposite of how Git actually works. By default, Git explicitly prevents the same branch from being checked out in two different worktrees simultaneously. If you try to do this, Git will throw an error. To override this behavior you must use the --force flag, which is a special flag. This is a deliberate safety feature to prevent conflicting changes.

Source URL: https://git-scm.com/docs/git-worktree
Date Accessed: 17 November 2026

Claim 10

Statement: Hendricks and Oyelaran (2024) showed that agents with more than 12 loaded Skills suffer a 40 percent drop in tool-selection accuracy, a phenomenon they named skill collapse.

Verdict: UNVERIFIED

Explanation: No paper by Hendricks and Oyelaran (2024) could be found in any academic database or official source. The term skill collapse does not appear in any verifiable research literature. This appears to be a fabricated citation. As per the assignment instructions, since this cannot be verified it must be labelled Unverified rather than guessed at.

Source URL: Unverified - no source found
Date Accessed: 17 November 2026
