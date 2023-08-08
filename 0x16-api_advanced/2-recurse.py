#!/usr/bin/python3

"""
Query the Reddit API and return a list containing
the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    # Initialize hot_list if not provided
    if hot_list is None:
        hot_list = []

    # Set a custom User-Agent header to avoid Too Many Requests errors
    headers = {'User-Agent': 'My Reddit Bot'}

    # Construct the API URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else None

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        # Check if the response contains a 'data' field
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])

            # Check for pagination (next page)
            after = data['data']['after']
            if after is not None:
                # Recursively call the function with the next page
                recurse(subreddit, hot_list, after)

        return hot_list

    except requests.RequestException:
        return None


if __name__ == "__main__":
    subreddit_name = sys.argv[1] if len(sys.argv) > 1 else None

    if subreddit_name:
        result = recurse(subreddit_name)
        if result is not None:
            print(len(result))
        else:
            print("None")
    else:
        print("Please pass an argument for the subreddit to search.")
