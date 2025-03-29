# server.py
from mcp.server.fastmcp import FastMCP
from atlassian import Jira
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

mcp = FastMCP("Demo")

@mcp.tool()
def get_jira_ticket_info(ticket_id: str) -> dict:
    """Get the info of a jira ticket.

    Args:
        ticket_id: The id of the jira ticket
        
    Returns:
        dict: Dictionary containing ticket information
        
    Raises:
        Exception: If ticket not found or API error occurs
    """
    try:
        jira = Jira(
            url=os.getenv("JIRA_URL"),
            username=os.getenv("JIRA_USERNAME"),
            password=os.getenv("JIRA_TOKEN"),
            cloud=True
        )
        issue = jira.issue(ticket_id)
        return {
            "id": ticket_id,
            "summary": issue.get("fields", {}).get("summary"),
            "status": issue.get("fields", {}).get("status", {}).get("name"),
            "description": issue.get("fields", {}).get("description")
        }
    except Exception as e:
        raise Exception(f"Error fetching Jira ticket {ticket_id}: {str(e)}")


if __name__ == "__main__":
    mcp.run(transport='stdio')