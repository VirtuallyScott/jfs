import requests
from .config import load_config

config = load_config()

def create_issue(issue_type, summary, description, assignee=None):
    # Implement the function to create a new JIRA issue
    pass

def move_issue(issue_key, transition_id):
    # Implement the function to move an issue through the workflow
    pass

def export_issues(jql, filename):
    # Implement the function to export issues to a CSV file
    pass

def import_issues(filename):
    # Implement the function to import issues from a CSV file
    pass
