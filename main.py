import requests
from collections import defaultdict
import os

# GitHub personal access token (set this as an environment variable for security)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Example: set via `export GITHUB_TOKEN=your_token`
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

def get_org_repos(org):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/orgs/{org}/repos?per_page=100&page={page}"
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code != 200:
            raise Exception(f"Failed to fetch repos: {resp.status_code} {resp.text}")
        data = resp.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return [repo['name'] for repo in repos]

def get_repo_authors(org, repo):
    authors = set()
    page = 1
    while True:
        url = f"https://api.github.com/repos/{org}/{repo}/commits?per_page=100&page={page}"
        resp = requests.get(url, headers=HEADERS)
        if resp.status_code == 409:  # Empty repo
            break
        if resp.status_code != 200:
            raise Exception(f"Failed to fetch commits for {repo}: {resp.status_code} {resp.text}")
        commits = resp.json()
        if not commits:
            break
        for commit in commits:
            commit_data = commit.get("commit", {})
            author_info = commit_data.get("author", {})
            name = author_info.get("name")
            email = author_info.get("email")
            if name and email:
                authors.add((name, email))
        page += 1
    return authors

def main():
    org = input("Enter GitHub organization name: ").strip()
    print(f"\nFetching repositories for organization '{org}'...\n")
    repos = get_org_repos(org)
    if not repos:
        print("No repositories found.")
        return

    for repo in repos:
        print(f"Repository: {repo}")
        try:
            authors = get_repo_authors(org, repo)
            if authors:
                for name, email in sorted(authors):
                    print(f"  - {name} <{email}>")
            else:
                print("  No authors found.")
        except Exception as e:
            print(f"  Error: {e}")
        print()

if __name__ == "__main__":
    main()
