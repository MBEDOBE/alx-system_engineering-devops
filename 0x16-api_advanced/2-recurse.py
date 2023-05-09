#!/usr/bin/python3
import requests
"""
function that queries reddit api
"""

def recurse(subreddit, hot_list=[], after=None):
    """
    recursive function that queries the reddit api and returns a list
    containing the titles of all hot articles for a given reddit.
    if no results are found for the given subreddit the function
    should return none
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        if len(hot_list) >= data["data"]["dist"]:
            return hot_list
        else:
            after = data["data"]["after"]
            return recurse(subreddit, hot_list, after)
    else:
        return None
