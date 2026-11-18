Plugin Installation Steps
Step 1: Add to Marketplace
Open Claude Code
Go to Settings
Click on Plugins
Click Add from local path
Navigate to the plugin/campus-helpdesk folder
Click Select Folder
Step 2: Install the Plugin
After adding, you will see campus-helpdesk appear in your plugins list
Click Install next to campus-helpdesk
Claude Code will read the manifest.json file
It will load the timetable-helper Skill automatically
It will register the /timetable slash command
It will activate the block-protected-writes hook
Step 3: Verify It Loaded

Run this command in Claude Code terminal to confirm the plugin loaded:

claude plugin list

You should see campus-helpdesk listed with status: active

Run this to verify the skill loaded:

claude skill list

You should see timetable-helper listed.

Run this to verify the slash command works:

/timetable Monday

You should see the Monday timetable returned.

Step 4: Uninstall the Plugin
Go to Settings
Click on Plugins
Find campus-helpdesk in the list
Click Uninstall
Confirm when prompted

Or run this command:

claude plugin remove campus-helpdesk

After uninstalling, verify it is gone by running:

claude plugin list

The campus-helpdesk entry should no longer appear.

Notes
Uninstalling the plugin does not delete your local files
The MCP server must be stopped separately if it is running
The hook is deactivated automatically when the plugin is uninstalled
