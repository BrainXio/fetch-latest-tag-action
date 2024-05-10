import os
import sys
import json
import subprocess

# Fetch required inputs
owner = sys.argv[1] if len(sys.argv) > 1 else ""
repo = sys.argv[2] if len(sys.argv) > 2 else ""

if not owner or repo:
    print("Error: Owner and Repo are required.")
    sys.exit(1)

# Fetch tags from the GitHub API
def fetch_tags(owner, repo):
    try:
        result = subprocess.run(
            ["curl", "-s", "-H", "Accept: application/vnd.github.v3+json",
             "-H", "User-Agent: GitHub-Action",
             f"https://api.github.com/repos/{owner}/{repo}/tags"],
            capture_output=True, text=True)
        result.check_returncode()
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error fetching tags: {e}")
        sys.exit(1)

# Find the latest tag, ignoring release candidates
def get_latest_tag(tags):
    non_rc_tags = [tag['name'] for tag in tags if '-rc' not in tag['name']]
    return non_rc_tags[0] if non_rc_tags else "No tags available"

tags = fetch_tags(owner, repo)
latest_tag = get_latest_tag(tags)

print(f"Latest tag: {latest_tag}")
print(f"::set-output name=latest-tag::{latest_tag}")
