#!/usr/bin/python3

"""
Queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces
"""


import requests
import re
from collections import Counter


def count_words(subreddit, word_list, after=None):
    # Initialize the Counter
    word_counter = Counter()

    # Set a custom User-Agent header to avoid Too Many Requests errors
    headers = {'User-Agent': 'My Reddit Bot'}

    # Construct the API URL for the subreddit's hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else None

    try:
        response = requests.get(url, headers=headers, params=params)
        # Raise an exception if the response status code is not 200
        response.raise_for_status()
        data = response.json()

        # Check if the response contains a 'data' field
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                for word in word_list:
                    # Use regular expression to match whole words only
                    word = word.lower()
                    pattern = rf'\b{re.escape(word)}\b'
                    if re.search(pattern, title.lower()):
                        word_counter[word] += 1

            # Check for pagination (next page)
            after = data['data']['after']
            if after is not None:
                # Recursively call the function with the next page
                count_words(subreddit, word_list, after)

        sorted_counts = sorted(word_counter.items(),
                               key=lambda item: (-item[1], item[0]))

        for word, count in sorted_counts:
            print(f"{word}: {count}")

    except (requests.RequestException,
            requests.HTTPError, requests.ConnectionError) as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    subreddit_name = sys.argv[1] if len(sys.argv) > 1 else None
    word_list = sys.argv[2:] if len(sys.argv) > 2 else []

    if subreddit_name and word_list:
        count_words(subreddit_name, word_list)
    else:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print(
            "Ex: {} programming 'python java javascript'".format(
                sys.argv[0]))
