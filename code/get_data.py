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

def get_relation(submission_id, top_author, all_replies, post_comments, comments):
    # while all_replies:
    #     reply = all_replies.pop(0)
    for reply in all_replies:
        post_comments_output = "{},{},{},{}\n".format(submission_id, reply.id, top_author, reply.author)
        comment_output = '{},{},{},"{}"\n'.format(submission_id, reply.id, reply.author, preprocess(reply.body))
        # print(post_comments_output)
        print(comment_output)
        post_comments.write(post_comments_output)
        comments.write(comment_output)


def main():
    api = PushshiftAPI()
    start_time = int(dt.datetime(2021, 1, 1).timestamp())
    # end_time = int(dt.datetime(2021, 3, 1).timestamp())
    submissions = api.search_submissions(after=start_time, before=1615383011,
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

    i = 200
    j = 5
    post_comments = open("{}{}.csv".format(post_comments_info,j),'a')
    posts = open("{}{}.csv".format(post_info,j),'a')
    comments = open("{}{}.csv".format(comment_info,j),'a')   
    for submission in submissions:
        if i == 200:
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

        submission_id = submission.id
        timestamp = submission.created_utc
        title = submission.title
        post_author = submission.author

        print("----------------------POSTS {}----------------------".format(i))  
        i += 1
        post_output = '{},{},{},{},"{}","{}"\n'.format(submission_id,timestamp,post_author,submission.url,title,preprocess(submission.selftext))
        print(post_output)
        posts.write(post_output)
        print("----------------------COMMENTS----------------------")
        cur_submission.comments.replace_more(limit=40000, threshold=5)
        comment_queue = cur_submission.comments[:]  # Seed with top-level
        print("The length of the top-level comments is {}".format(len(comment_queue)))
        while comment_queue:
            comment = comment_queue.pop(0)
            comment_author = comment.author
            comment_id = comment.id
            comment_text = comment.body
            if comment_text == "[deleted]":
                continue
            post_comments_output = "{},{},{},{}\n".format(submission_id, comment_id, post_author, comment_author)
            comment_output = '{},{},{},"{}"\n'.format(submission_id, comment_id, comment_author, preprocess(comment_text))
            # print(post_comments_output)
            print(comment_output)
            post_comments.write(post_comments_output)
            comments.write(comment_output)
            reply_queue = comment.replies
            get_relation(submission_id, comment_author, reply_queue, post_comments, comments)
            comment_queue.extend(comment.replies)
        # for comment in cur_submission.comments.list():
        #     post_comments_output = "{},{},{}\n".format(submission.id, submission.author, comment.author)
        #     post_comments.write(post_comments_output)
        #     comment_output = '{},{},"{}"\n'.format(submission.id, comment.author, preprocess(comment.body))
        #     comments.write(comment_output)
        #     print(comment_output)
    
    
if __name__ == '__main__':
    main()
