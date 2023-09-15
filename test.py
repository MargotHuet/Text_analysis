from textblob import TextBlob 

with open('monTexte.txt', 'r') as f:
    text = f.read()

    
blob = TextBlob(text)
sentiment = blob.sentiment.polarity # Notation entre -1 et 1
print(sentiment)