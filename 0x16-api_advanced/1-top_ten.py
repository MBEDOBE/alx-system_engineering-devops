#!/usr/bin/python3
import requests
"""
a functions that queries the reddit api
"""

def top_ten(subreddit):
    """
    function definition that prints the titles of first 10 hot posts listed
    for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"][:10]:
            print(post["data"]["title"])
    else:
        print(None)
