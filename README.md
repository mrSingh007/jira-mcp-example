 With uv https://docs.astral.sh/uv/getting-started/ tool first set the env
 1. Rum `uv init` then `uv venv` to your new directory
 3. Now install mcp with `uv pip install mcp`
 4. Install atlassian library `uv pip install atlassian-python-api`
 5. Open the main.py file and replace code with [THIS](/main.py)
 6. In your project directory add `.cursor/mcp.json` file with following content
```
{
  "mcpServers": {
    "jira-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "<PATH_TO_YOUR_main.py_FILE_FOLDER>,
        "run",
        "main.py"
      ],
      "env": {
        "JIRA_URL": "<JIRA_URL>",
        "JIRA_USERNAME": "<JIRA_EMAIL>",
        "JIRA_TOKEN": "<TOKEN>"
      }
    }
  }
}

```
7. Go to cursor setting and enable the MCP
Thats it :) In chat box ask about your jira tickets
