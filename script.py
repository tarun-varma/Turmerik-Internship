import praw
import pandas as pd

# Reddit API credentials
reddit_client_id = 'vdUhKewN6IcSjoVUI1wxeg'
reddit_client_secret = '5LsHBrz-IDw_RiT0OiGmOMO5tKgAnA'
reddit_user_agent = 'Scraping App'

# Authenticate with Reddit's API
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent)

# List of subreddits related to health conditions and clinical trials
subreddit_list = ['health', 'medicine', 'clinicaltrials', 'AskDocs']

# Create an empty list to store the scraped data
data = []

# Iterate over each subreddit
for subreddit_name in subreddit_list:
    subreddit = reddit.subreddit(subreddit_name)
    
    print("Scraping posts from r/{}...".format(subreddit_name))
    
    # Iterate over hot posts in the subreddit
    for submission in subreddit.hot(limit=200):
        title = submission.title
        score = submission.score
        url = submission.url
        
        # Iterate over comments in each post
        submission.comments.replace_more(limit=None)
        comments = []
        for comment in submission.comments.list():
            comments.append(comment.body)
        
        # Append the data to the list
        data.append({'Subreddit': subreddit_name,
                     'Title': title,
                     'Score': score,
                     'URL': url,
                     'Comments': comments})

# Convert the list of dictionaries to a DataFrame
df = pd.concat([pd.DataFrame(data[i]) for i in range(len(data))], ignore_index=True)

# Save the DataFrame as a CSV file
df.to_csv('Data/reddit_data.csv', index=False)

print("Data saved successfully!")
