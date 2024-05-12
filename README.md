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

### Challenges
1. Handling large volumes of data while scraping Reddit.
2. Ensuring accuracy and reliability of sentiment analysis results.
3. Fine-tuning the AI model to generate coherent and contextually appropriate messages.

## Examples
**Data Collected** - Example Reddit posts and comments related to clinical trials.
The Python script (Script.py) utilizes the PRAW library to scrape data from Reddit, focusing on subreddits relevant to health conditions and clinical trials. It authenticates with Reddit's API using provided credentials and iterates over each subreddit, extracting information such as post titles, scores, URLs, and comments. The script aggregates this data into a structured format, converting it into a Pandas DataFrame, and saves it as a CSV file named 'reddit_data.csv'. This approach enables the collection of a diverse range of opinions and discussions from Reddit users, providing valuable insights into their attitudes and interests regarding clinical trials and health-related topics.

**Sentiment Analysis Results** - Visualizations showcasing sentiment distributions across different sentiment groups.
Number of comments with positive opinions: 10467
Number of comments with neutral opinions: 6043
Number of comments with negative opinions: 4974
![image](https://github.com/tarun-varma/Turmerik-Internship/assets/77658822/1ea095e6-eae8-4c39-a65c-b0d4dfe29f51)


**Personalized Messages generated** - Examples of personalized messages generated for positive, neutral, and negative sentiment groups.

I ran out of credits for the OpenAI API so was unable to generate personalized messages but I have the idea on how to do this and will explain about it.





