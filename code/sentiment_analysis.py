from textblob import TextBlob
import json
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


comments_raw_json_1 = open('comments.json')
comments_raw_json_2 = open('comments_2.json')

comments_json_1 = json.load(comments_raw_json_1)
comments_json_2 = json.load(comments_raw_json_2)

raw_comments = comments_json_1 + comments_json_2

# Sample comments and ratings (replace with your actual data)
comments = [raw_comment['text'] for raw_comment in raw_comments]
ratings = [raw_comment['rating'] for raw_comment in raw_comments]

# Preprocess data
def preprocess(text):
    text = text.lower()
    words = word_tokenize(text)
    words = [word for word in words if word.isalpha() and word not in stopwords.words('english')]
    return words

# Calculate sentiment scores
sentiment_scores = []
for comment in comments:
    words = preprocess(comment)
    sentiment = TextBlob(comment).sentiment.polarity
    sentiment_scores.append(sentiment)

# Calculate average sentiment scores for each word
word_sentiment_dict = {}
for i, words in enumerate(map(preprocess, comments)):
    for word in set(words):
        if word not in word_sentiment_dict:
            word_sentiment_dict[word] = [sentiment_scores[i]]
        else:
            word_sentiment_dict[word].append(sentiment_scores[i])

# Calculate average sentiment scores for each word
average_word_sentiment = {word: sum(scores) for word, scores in word_sentiment_dict.items()}

# Rank words based on sentiment scores
sorted_words_positive = sorted(average_word_sentiment.items(), key=lambda x: x[1], reverse=True)
sorted_words_negative = sorted(average_word_sentiment.items(), key=lambda x: x[1])

# Display top N words for positive and negative sentiments
top_n = 50
print(f"Top {top_n} words for positive sentiment:")
print(sorted_words_positive[:top_n])

print(f"\nTop {top_n} words for negative sentiment:")
print(sorted_words_negative[:top_n])

