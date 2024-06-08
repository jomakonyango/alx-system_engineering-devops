#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    """
    # Set custom User-Agent
    headers = {'User-Agent': 'my-app/0.0.1'}

    # Send a GET request to the Reddit API
    response = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers=headers,
        allow_redirects=False
    )

    # Check if the subreddit is valid
    if response.status_code != 200:
        return 0

    # Get the number of subscribers
    data = response.json()
    return data['data']['subscribers']
