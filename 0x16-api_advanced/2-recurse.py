#!/usr/bin/python3

"""
Query the Reddit API and return a list containing
the titles of all hot articles for a given subreddit
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """set User-Agent and fetch with a limit :100"""
    headers = {'User-Agent': 'levittC17'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()

        data = response.json().get('data', {})
        posts = data.get('children', [])

        if posts:
            hot_list.extend([post['data']['title'] for post in posts])
            after = data.get('after')
            if after:
                recurse(subreddit, hot_list, after)
        else:
            print("No posts found.")
            return None

        return hot_list
    except requests.exceptions.RequestException:
        return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please provide a subreddit name as an argument.")
    else:
        subreddit_name = sys.argv[1]
        result = recurse(subreddit_name)
        if result is not None:
            print(len(result))
        else:
            print("None")
