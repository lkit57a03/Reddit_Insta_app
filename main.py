import memes_dowloader
import meme_uploader
import update_csv
import os
import sys


if __name__ == "__main__":
    subreddit = sys.argv[1:]
    username = os.environ["{}_username".format(sys.argv[1])]
    password = os.environ["{}_password".format(sys.argv[1])]
    #download new memes content
    memes_list = memes_dowloader.get_posts(subreddit)
    update_csv.write_memes_to_file(memes_list=memes_list,subreddit_name=subreddit)  
    val = meme_uploader.check_for_non_uploaded_and_upload(username, password, subreddit_name=subreddit)

    while not val:
        val = meme_uploader.check_for_non_uploaded_and_upload(username, password, subreddit_name=subreddit)
    print(val)
    pass