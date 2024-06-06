#!/usr/bin/python3
"""
0-subs
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    """
    # Set custom User-Agent
    headers = {'User-Agent': 'my-app/0.0.1'}

    # Send a GET request to the Reddit API
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code != 200:
        return 0

    # Parse the response and get the number of subscribers
    data = response.json()
    return data['data']['subscribers']
