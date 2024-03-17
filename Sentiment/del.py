import pandas as pd
df = pd.DataFrame(pd.read_csv('combined_sentiment_score.csv'))
df['SentimentScore_Roberta'] = (df['SentimentScore_Roberta'] * 2) - 1

df.to_csv("sentiment_score.csv", index=False) 
