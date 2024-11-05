from textblob import TextBlob
import pandas as pd
def overall_analysis(filepath:str):

# Load your dataset
# Assuming your dataset is in a CSV file and the review content is in a column named 'review_content'
# Adjust the file path and column name accordingly
    df = pd.read_csv(filepath)

    # Concatenate all reviews into a single text
    all_reviews = ' '.join(df['title'])

    # Perform sentiment analysis on the concatenated text
    overall_sentiment = TextBlob(all_reviews).sentiment.polarity

    # Classify the overall sentiment based on the polarity
    if overall_sentiment > 0:
        overall_sentiment_label = 'Positive'
    elif overall_sentiment < 0:
        overall_sentiment_label = 'Negative'
    else:
        overall_sentiment_label = 'Neutral'

    # Display the overall sentiment label
    print(f"Overall Sentiment: {overall_sentiment_label}")
def each_title_analysis(filepath:str):

# Load your dataset
# Assuming your dataset is in a CSV file and the review content is in a column named 'review_content'
# Adjust the file path and column name accordingly
    df = pd.read_csv(filepath)

    # Function to perform sentiment analysis on each review
    def analyze_sentiment(review):
        analysis = TextBlob(review)
        # Classify the sentiment based on the polarity
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity < 0:
            return 'Negative'
        else:
            return 'Neutral'

    # Apply sentiment analysis to each review in the dataset
    df['sentiment'] = df['title'].apply(analyze_sentiment)

    # Display the results
    print(df[['title', 'sentiment']])
