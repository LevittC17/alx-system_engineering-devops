#!/usr/bin/python3

"""
Query the Reddit APIand print the titles of the
first 10 hot posts listed for a given subreddit
"""


import requests


def top_ten(subreddit):
    """Set a custom User-Agent header to avoid Too Many Requests errors"""
    headers = {'User-Agent': 'My Reddit Bot'}

    # construct the API URL for the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        # check if the response contains a 'data' fiield
        if 'data' in data:
            # extract the first 10 posts
            posts = data['data']['children'][:10]

            for post in posts:
                print(post['data']['title'])
            else:
                print('None')

    except requests.RequestException:
        print('None')


if __name__ == "__main__":
    subreddit_name = sys.argv[1] if len(sys.argv) > 1 else None

    if subreddit_name:
        top_ten(subreddit_name)
    else:
        print('Please pass an argument for the subreddit to search')
