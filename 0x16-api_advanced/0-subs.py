#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers
for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    # Define the User-Agent to avoid being blocked by Reddit's API
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    # Define the URL for Reddit API request
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Send the request
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the response status code is 200 OK
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            # Extract the number of subscribers
            return data.get('data', {}).get('subscribers', 0)
        else:
            # If status code is not 200, subreddit might be invalid
            return 0
    except Exception:
        # Handle other exceptions (e.g., network issues)
        return 0

