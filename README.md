# Sentiment Analysis and Personalized Messaging for Clinical Trial Recruitment
This project aims to demonstrate the utilization of sentiment analysis and AI-driven personalized messaging to identify potential participants for a clinical trial by analyzing sentiments expressed on Reddit.

## Setup Instructions
### 1. Clone the repository
git clone https://github.com/tarun-varma/Turmerik-Internship.git

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the code
Execute scripts.py which scrapes the data from reddit using praw.
Run "python3 scripts.py"

This will save the required dataset having posts related to clinical trails in the Data folder.

## Methodology and Challenges
1. **Data Collection** - Utilized PRAW (Python Reddit API Wrapper) to scrape relevant subreddits for posts and comments about clinical trials.
2. **Sentiment Analysis** - Employed TextBlob for sentiment analysis to gauge user opinions and receptiveness towards clinical trials.
3. **Message Generation** - Utilized the OpenAI API to generate personalized messages aimed at users expressing interest in or potentially benefiting from participating in a clinical trial.




