# 0x16. API advanced

## Description
This repository contains Python functions that interact with the Reddit API to retrieve information about subreddits. There are three functions:

---

### [0. How many subs?](./0-subs.py)
* number_of_subscribers(subreddit): 
This function queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function returns 0.


### [1. Top Ten](./1-top_ten.py)
* top_ten(subreddit): 
This function queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. If an invalid subreddit is given, the function prints None.


### [2. Recurse it!](./2-recurse.py)
* recurse(subreddit, hot_list=[]):
This recursive function queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function returns None.

All functions use the requests library to send HTTP requests to the Reddit API and parse the JSON responses. They also use a custom User-Agent header to avoid the "Too Many Requests" error.

Note that invalid subreddits may return a redirect to search results. The functions are designed to avoid following redirects.

Feel free to use and modify these functions for your own projects!


---

## Author
* **Daniel Mbedobe** - [mbedobe](https://github.com/mbedobe)


