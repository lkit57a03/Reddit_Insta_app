import praw

reddit = praw.Reddit(client_id='cYutN672JNJ_8Q',client_secret='q0K95MT8tTmyJCIiC35U6D8d7oM',user_agent='Harsh_Tiwari')

def get_posts(subreddit_names):
        found=[]
        for sub_name in subreddit_names:
            print (sub_name)
            for sub in reddit.subreddit(sub_name).hot(limit=100):
                meme_data = {"id":sub.id,"title":sub.title,"url":sub.url,"score":sub.score,"uploaded":False}
                found.append(meme_data)
        # print(found)
        return found
