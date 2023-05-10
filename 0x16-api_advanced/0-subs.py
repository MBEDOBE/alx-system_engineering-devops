#!/usr/bin/python3
import requests
"""
a function that queries reddit api and returns number
of subs
"""


def number_of_subscribers(subreddit):
    """
    function definition of getting number of subs
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return int(data["data"]["subscribers"])
    else:
        return 0
