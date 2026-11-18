Part E: Parallel Development with Worktrees
Commands Used and Output
Creating the Three Worktrees

git branch feature/skill-tests
git branch feature/mcp-server
git branch bugfix/hook-path
git worktree add ../feature-skill-tests feature/skill-tests
git worktree add ../feature-mcp-server feature/mcp-server
git worktree add ../bugfix-hook-path bugfix/hook-path

Worktree List Output

/Users/lokeshrathod12/Desktop/campus-helpdesk-assignment e159fcd [main]
/Users/lokeshrathod12/Desktop/bugfix-hook-path e159fcd [bugfix/hook-path]
/Users/lokeshrathod12/Desktop/feature-mcp-server e159fcd [feature/mcp-server]
/Users/lokeshrathod12/Desktop/feature-skill-tests e159fcd [feature/skill-tests]

Merge Conflict and Resolution

A merge conflict was deliberately created by adding a file called shared.md with different content in feature/skill-tests and feature/mcp-server branches.

Conflict message received:
CONFLICT (add/add): Merge conflict in shared.md
Automatic merge failed; fix conflicts and then commit the result.

Resolution: The conflict was resolved by writing a combined version and committing it.

Conceptual Questions
(a) Why Git refuses to check out one branch in two worktrees by default

Git refuses to check out the same branch in two different worktrees because each worktree has its own HEAD file that points to the current branch. If two worktrees shared the same branch, they would both be modifying the same set of tracked files and the same HEAD pointer simultaneously. This would cause conflicts and data corruption because changes in one worktree would immediately affect the other. Git enforces this as a safety measure to maintain integrity of the working directories.

(b) What is shared and what is not shared between worktrees

Shared between all worktrees:

The .git object database (all commits, trees, blobs)
All branches and tags
The git config file
Stash entries

Not shared between worktrees:

The working directory files
The HEAD file (each worktree has its own)
The index/staging area
node_modules folders
Environment files like .env
Any untracked local files
(c) How to clean up stale worktrees safely

A stale worktree is one whose directory has been deleted manually without using git worktree remove. To clean them up safely:

Step 1 - Run git worktree list to see all worktrees and identify stale ones
Step 2 - Run git worktree prune to automatically remove stale worktree references
Step 3 - For worktrees that are still present, run git worktree remove <path> to remove them cleanly
Step 4 - Run git worktree list again to confirm they are gone

Never delete the .git/worktrees folder manually as this can corrupt the repository.

Evaluation of CTO Statement

The CTO writes: “Use the built-in /worktree-merge command in Claude Code, which resolves conflicts across worktrees automatically, so no manual review is needed.”

This statement is FALSE for two reasons:

First, there is no built-in command called /worktree-merge in Claude Code. This command does not exist. Claude Code does not have a dedicated worktree merge command. This is a fabricated claim similar to the other fabricated claims in this assignment.

Second, even if such a command existed, the idea of letting an AI agent resolve merge conflicts automatically without human review is dangerous. Merge conflicts represent disagreements between two versions of code or content. Resolving them requires understanding the intent behind each change. An AI agent cannot know which version is correct without context from the developer. Automatic resolution without review risks introducing bugs, losing important changes, or silently choosing the wrong version. Human review of merge conflicts is a fundamental software engineering practice that should never be delegated entirely to an automated system.