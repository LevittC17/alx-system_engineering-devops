#!/usr/bin/python3

"""
Query the Reddit APIand print the titles of the
first 10 hot posts listed for a given subreddit
"""


import requests
import sys


def top_ten(subreddit):
    """ Fetches the top ten post titles from a subreddit """
    headers = {'User-Agent': 'my_custom_user_agent'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, timeout=10)
        response.raise_for_status()

        data = response.json().get('data', {}).get('children', [])
        if data:
            for post in data:
                print(post['data']['title'])
        else:
            print("No posts found.")
    except requests.exceptions.RequestException as e:
        print('None')


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No argument passed for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
