from textblob import TextBlob

text = [
    "i love NLP ! It's works great and ",
    "this my first experience,i am little bit dissapointed",
    "it is very quiet interresting it is neither good or bad",
]

# create function
def analyze_sentiment(text):
    analysis = TextBlob(text)
    #-1.0-1.0
    polarity =analysis.sentiment.polarity
    if polarity>0:
       return "Positive"
    elif polarity<0:
        return "Negative"
    else:
        return "Neutral"
        return sentiment
for text in text:
    sentiment = analyze_sentiment(text)
    print(f"Text:{text}")
    print(f"Sentiment:{sentiment}\n")