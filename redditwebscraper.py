!pip install praw
#%%
import csv
import praw

reddit = praw.Reddit(client_id='y1sxdAoN0b-gZQ',
                     client_secret='56YAQAahxq8XsSR8rakv1nv7y-sOIA',
                     user_agent='Webscraper')


# get 10 hot posts from the MachineLearning subreddit

topics=['gaming','music','science','movies','food','news','sports','books','history']
temporarylist=[]
for topic in topics:
    
    hot_posts = reddit.subreddit(topic).top("all",limit=500)

    for post in hot_posts:
        if len(post.selftext)>0:
            temporarylist.append([post.title.replace('\n','') + '. ' +  post.selftext.replace('\n','')])
        else:
            temporarylist.append([post.title.replace('\n','')])
    
with open('alltopicsbutfitness.csv', 'w',newline ='',encoding="utf-8") as f: 
    write = csv.writer(f) 
    write.writerows(temporarylist)
