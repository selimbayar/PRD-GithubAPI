"""
This file takes a link of any repository on github and displays information
about the number of stars, forks, contributors, etc.

This file can be used anytime regardless of the other files

"""

import json

import requests
import os

# setup access_token, and headers

access_token = os.getenv('GITHUB_TOKEN', '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')
headers = {'Authorization': "Token " + access_token}

# Enter the API link of desired repo to get its info
url = "https://api.github.com/repos/CompVis/stable-diffusion"


# API call for the specified URL

repo = requests.get(query_url, headers=headers)

# Turn the data into a json file

repo_json_file = repo.json()

# Total number of Star

star_count = repo_json_file['stargazers_count']
print(f"Star count: {star_count}")

# Total number of Fork

forks_count = repo_json_file['forks_count']
print(f"Fork count: {forks_count}")

# Total number of Watch

watchers_count = repo_json_file['subscribers_count']
print(f"Watchers count: {watchers_count}")

# Total number of Issues

issues_count = repo_json_file['open_issues_count']
print(f"Issues count: {issues_count}")

# Total number of Contributors

contributors_url = repo_json_file['contributors_url']
contributors = requests.get(contributors_url, headers=headers)
contributors_file = contributors.json()
contributors_count = len(contributors_file)
print(f"Contributors count: {contributors_count}")


# Total number of commits for each contributor

commits_url = repo_json_file['commits_url']
commits = requests.get(commits_url[:-6], headers=headers)
commits_file = commits.json()
for user in contributors_file:
    count = 0
    for commit in commits_file:
        if user['login'] == commit['author']['login']:
            count += 1
    print(f"Total number of commits for " + user['login'] + ": " + str(count))

# Last commit date for each contributor

for user in contributors_file:
    for commit in commits_file:
        if user['login'] == commit['author']['login']:
            print(f"Last commit date for " + user['login'] + ": " + commit['commit']['author']['date'])
            break

# Total number of changed files for each contributor

# Total number of additions for each contributor

# Total number of deletions for each contributor
