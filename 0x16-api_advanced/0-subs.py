#!/usr/bin/python3
"""
a function that queries reddit api and returns number of subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    function definition of getting number of subs
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return (0)
    data = response.json()
    if "data" in response:
        return (response.get("data").get("subscribers"))
    else:
        return 0
