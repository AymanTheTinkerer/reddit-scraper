# reddit-scraper

## About
This scraper was created to scrape posts and their comments from subreddits as part of a research project I worked on under Hayeong Song. It makes use of the PRAW API.

## Usage
To run this scraper, make sure to first go to https://www.reddit.com/prefs/apps and create your own app. Then find the client id, client secret, and user agent and replace this information on line 6 using your personal IDs that you just obtained. See https://www.honchosearch.com/blog/seo/how-to-use-praw-and-crawl-reddit-for-subreddit-post-data/ for more information

## Run
To run the scraper, make sure you have python installed on your computer and run ``` python scraper.py ``` through terminal or command prompt in the same directory as the scraper.

## Modifying the scraper
This scraper can easily be modified to get different types of information. For example, you change the subreddit name in line 8 to scrape a completely different subreddit. Moreover, modifying the limit in line 16 can allow you to scrape a greater amount of posts, with a limit of a 1000 posts at a time. The for loop can also be modified to scrape comments from the 'hot' or 'controverisal' section of a subreddit. There are many more ways to modify the scraper and more information can be found on PRAW's documentations: https://praw.readthedocs.io/en/stable/

## Limitations
As mentioned previously, PRAW only allows for a maximum of 1000 posts to be scraped at a time, with a limit of 30 comments per post. 