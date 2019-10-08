import praw

reddit = praw.Reddit(client_id='cYutN672JNJ_8Q',client_secret='q0K95MT8tTmyJCIiC35U6D8d7oM',user_agent='Harsh_Tiwari')

def get_posts():
        found=[]
        for sub in reddit.subreddit('memes').hot(limit=20):
            meme_data = {"id":sub.id,"title":sub.title,"url":sub.url,"score":sub.score,"uploaded":False}
            found.append(meme_data)
        # print(found)
        return found
