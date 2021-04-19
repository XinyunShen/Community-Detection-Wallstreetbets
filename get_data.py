from psaw import PushshiftAPI
import datetime as dt
from IPython import display
import math
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import praw
from praw.models import MoreComments


def preprocess(text):
    text = text.split('\n')
    text = ' '.join(text)
    return text

def main():
    api = PushshiftAPI()
    start_time = int(dt.datetime(2021, 1, 1).timestamp())
    end_time = int(dt.datetime(2021, 3, 1).timestamp())
    submissions = api.search_submissions(after=start_time, before=end_time,
                                        subreddit='wallstreetbets',
                                        filter=['id','url', 'selftext','author', 'title', 'domain'])
    reddit = praw.Reddit(client_id='8N3Jm_LZUT-sjQ',
                        client_secret='drCsZJL7XTkh_WH09aEzSGe8aeLMSA',
                        user_agent='Alyssa_yun')

    # get post author and its comments author to calculate pagerank including postid
    # get post id, post's text, author, time
    # get post id, comments' text, comments' text
    post_comments_info = "post_comments_info"
    post_info = "post_info"
    comment_info = "comment_info"

    i = 1000
    j = 0
    post_comments = open("{}{}.csv".format(post_comments_info,j),'a')
    posts = open("{}{}.csv".format(post_info,j),'a')
    comments = open("{}{}.csv".format(comment_info,j),'a')   
    for submission in submissions:
        if i == 1000:
            j += 1
            i = 0
            post_comments = open("{}{}.csv".format(post_comments_info,j),'a')
            posts = open("{}{}.csv".format(post_info,j),'a')
            comments = open("{}{}.csv".format(comment_info,j),'a')   

        if submission.domain != "self.wallstreetbets":
            continue
        cur_submission = reddit.submission(id=submission.id)
        if cur_submission.removed_by_category is None:
            print("The post is available.")
        elif cur_submission.removed_by_category in ('author', 'moderator'):
            print("The post is removed.")
            continue
        elif cur_submission.removed_by_category == 'deleted':
            print("The post is deleted.")
            continue
        else:
            print(f"Unknown post state: {cur_submission.removed_by_category}")
            continue

        print("----------------------POSTS {}----------------------".format(i))  
        i += 1
        post_output = '{},{},{},{},"{}","{}"\n'.format(submission.id,submission.created_utc,submission.author,submission.url,submission.title,preprocess(submission.selftext))
        print(post_output)
        posts.write(post_output)
        print("----------------------comments----------------------")
        cur_submission.comments.replace_more(limit=None)
        for comment in cur_submission.comments.list():
            post_comments_output = "{},{},{}\n".format(submission.id, submission.author, comment.author)
            post_comments.write(post_comments_output)
            comment_output = '{},{},"{}"\n'.format(submission.id, comment.author, preprocess(comment.body))
            comments.write(comment_output)
            print(comment_output)
    
if __name__ == '__main__':
    main()