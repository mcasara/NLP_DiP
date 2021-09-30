import csv
import praw
import random
reddit = praw.Reddit(client_id='y1sxdAoN0b-gZQ',
                     client_secret='56YAQAahxq8XsSR8rakv1nv7y-sOIA',
                     user_agent='Webscraper')


# get 10 hot posts from the MachineLearning subreddit

topics=['science','food','books']
temporarylist=[]
for topic in topics:
    
    hot_posts = reddit.subreddit(topic).top("year",limit=1000)

    for post in hot_posts:
        #if len(post.selftext)>0:
          #  temporarylist.append([post.title.replace('\n','')+'. '+post.selftext.replace('\n','')])
        #else:
            temporarylist.append([post.title.replace('\n',''),topic])
            
        
random.shuffle(temporarylist)

#%%

  
  
# field names  
fields = ['Content', 'Topic']
    
# data rows of csv file  

  
with open('3topicstitleonly.csv', 'w', newline='',encoding='utf-8') as f: 
      
    write = csv.writer(f,delimiter=',') 
    write.writerow(fields) 
    write.writerows(temporarylist)
