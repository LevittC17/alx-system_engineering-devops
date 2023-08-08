#!/usr/bin/python3

"""
Query the Reddit API and return the number of
subscribers - total subscribers
"""


import requests


def number_of_subscribers(subreddit):
    """Set a custom User-Agent header to avoid Too Many Requests errors"""
    headers = {'User-Agent': 'My Reddit Bot'}

    # Construct the APIA URL for the subreddit's information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        # Check if the response contains a 'data' field
        if 'data' in data:
            return data['data']['subscribers']
        else:
            # Return 0 for invalid subreddits or other errors
            return 0

    except requests.RequestException:
        # Return 0 if there's an issue with the request
        return 0


if __name__ == "__main__":
    subreddit_name = sys.argv[1] if len(sys.argv) > 1 else None

    if subreddit_name:
        subscribers_count = number_of_subscribers(subreddit_name)
        print(subscribers_count)
    else:
        print('Please pass an argument for the subreddit to search.')
