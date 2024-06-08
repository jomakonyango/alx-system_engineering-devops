#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    # Set custom User-Agent
    headers = {'User-Agent': 'linux:0x16_API_advanced:v1 (by /u/john_otieno)'}

    # Send a GET request to the Reddit API
    response = requests.get(
        'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit),
        headers=headers,
        allow_redirects=False
    )

    # Check if the subreddit is valid
    if response.status_code != 200:
        print(None)
        return

    # Get the titles of the first 10 hot posts
    data = response.json()
    for post in data['data']['children']:
        print(post['data']['title'])
