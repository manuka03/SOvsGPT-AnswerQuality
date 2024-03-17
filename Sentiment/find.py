import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("combined_sentiment_score.csv")  # Update with your CSV filename

# Plot histograms of sentiment scores
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(data['SentimentScore_Vader'], bins=20, color='blue', alpha=0.7)
plt.title('Vader Sentiment Score Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(data['SentimentScore_TextBlob'], bins=20, color='orange', alpha=0.7)
plt.title('TextBlob Sentiment Score Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Determine thresholds
vader_threshold = 0.5  # Example threshold for Vader sentiment score
textblob_threshold = 0.1  # Example threshold for TextBlob sentiment score

# Classify comments based on thresholds
data['Toxicity_Vader'] = data['SentimentScore_Vader'] >= vader_threshold
data['Toxicity_TextBlob'] = data['SentimentScore_TextBlob'] >= textblob_threshold

# Save the updated dataframe with toxicity labels
data.to_csv("data_with_toxicity_labels.csv", index=False)
