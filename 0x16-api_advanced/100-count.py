#!/usr/bin/python3

"""
Queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces
"""


import requests


def count_words(subreddit, word_list, after='', word_dict=None):
    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    if after is None:
        print_counts(word_dict)
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'my_custom_user_agent'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        response.raise_for_status()
        data = response.json().get('data', {})
        hot_posts = data.get('children', [])
        new_after = data.get('after')

        for post in hot_posts:
            title = post['data']['title'].lower()
            for word in word_dict:
                word_dict[word] += title.count(word)

        count_words(subreddit, word_list, new_after, word_dict)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


def print_counts(word_dict):
    sorted_counts = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count:
            print(f"{word}: {count}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        subreddit_name = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit_name, word_list)
