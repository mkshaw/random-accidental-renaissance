"""

get_art.py

Collect a sample of posts from r/AccidentalRenaissance/hot (top 20), then pick 1 from that sample.

Take args: sample size

Return: would be cool to return photo, for now put it in the /data directory. In future, serve to web?

"""

import json
import argparse
import requests
import os.path as osp
import random # for generating random number
import webbrowser # for launching photo in web browser

script_dir = osp.dirname(__file__)

def get_posts(subreddit, filt, sample_size, username, random_number):

    data = requests.get(f'http://api.reddit.com/r/{subreddit}/{filt}?limit={sample_size}', headers={'User-Agent': f'windows: requests (by /u/{username}'})
    content = data.json()['data']['children'][random_number]['data']
    return(content['url'])

def main():
    
    # define arguments to function
    parser = argparse.ArgumentParser()
    parser.add_argument('sample_size', help='Size of sample to retrieve from subreddit.')
    parser.add_argument('filter', help='Filter to apply to subreddit. e.g., hot, new, top.')
    parser.add_argument('subreddit', help='Subreddit to retrieve posts from, formatted as just the name (no "r/").')
    parser.add_argument('username', help='Username of person making the call.')

    args = parser.parse_args()

    # generate random number between 1 and 20
    random_number = random.randint(1, int(args.sample_size))

    # collect posts from reddit
    art_url = get_posts(args.subreddit, args.filter, args.sample_size, args.username, random_number)
    print(art_url)

    # open photo in default web browser
    # TODO caching, if you want to save the photos
    print(f'launching art webbrowser: {webbrowser.open(art_url, new=1)}')

if __name__ == '__main__':
    main()
