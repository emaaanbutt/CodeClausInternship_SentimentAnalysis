from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"


print("\nWelcome to Sentiment Analyzer!")
print("Type your sentence to analyze it. Type 'exit' to quit.\n")

while True:
    user_input = input("Sentence : ")
    if user_input.lower() == "exit":
        print("Goodbye!👋\n")
        break

    sentiment = analyze_sentiment(user_input)
    print("Sentiment: ", sentiment, "\n")
    
