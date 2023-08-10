import tweepy
from textblob import TextBlob

# Set up your Twitter API credentials
consumer_key = "KiOEYLeYZg5CwocKGUU3cK9s2"
consumer_secret = "Wc4qNPWNJwjqIWps76DWbboz2gm7rFAZxplD5hwuw0GLjjmHN9"
access_token = "1613527017882017797-aLEVvszAwOEBZA2CwXVaDEUVw3BTfG"
access_token_secret = "L6COJxXAVPlndNluigoDkFfvsaKb31ptDXqszHqIDUcd1"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define a listener class for real-time tweets
class SentimentAnalysisListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            tweet_text = status.text
            analysis = TextBlob(tweet_text)
            sentiment_score = analysis.sentiment.polarity

            if sentiment_score > 0:
                sentiment = "Positive"
            elif sentiment_score < 0:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            print(f"Tweet: {tweet_text}")
            print(f"Sentiment: {sentiment} (Score: {sentiment_score:.2f})")
            print("=" * 50)

        except Exception as e:
            print("Error:", str(e))

    def on_error(self, status_code):
        if status_code == 420:
            return False


# Create an instance of the listener and start streaming
listener = SentimentAnalysisListener()
stream = tweepy.Stream(auth=api.auth, listener=listener)

# Track specific keywords or hashtags for real-time analysis
track_keywords = ["COVID19", "vaccine", "pandemic"]
stream.filter(track=track_keywords)
