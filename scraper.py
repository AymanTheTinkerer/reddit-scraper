import praw
import pandas as pd
import private

#get this data from reddit https://www.reddit.com/prefs/apps -> create app
reddit = praw.Reddit(client_id=private.client_id, client_secret=private.client_secret, user_agent=private.user_agent)

subreddit = reddit.subreddit('climatechange')

submission = reddit.submission(id="u232nu")

posts_dict = {"Title":[],"score":[], "id":[], "subreddit":[], "url":[], "num_comments":[], "body":[], "comments": [""]}

ind = 0

for post in subreddit.new(limit=3):
    posts_dict["Title"].append(post.title)
    posts_dict["score"].append(post.score)
    posts_dict["id"].append(post.id)
    posts_dict["subreddit"].append(post.subreddit)
    posts_dict["url"].append(post.url)
    posts_dict["num_comments"].append(post.num_comments)
    posts_dict["body"].append(post.selftext)
    for comment in post.comments:
        posts_dict["comments"][ind] += comment.body + "\n"
    posts_dict["comments"].append("")  
    ind += 1

posts_dict["comments"].pop()
scraped = pd.DataFrame(posts_dict)
# scraped.to_csv("scraped2.csv", index=True)
print(posts_dict)