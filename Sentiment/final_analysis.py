import pandas as pd
def classify(score):
    if score<=-0.25:
        return 'Negative'
    elif score>0.25:
        return 'Positive'
    else: 
        return 'Neutral'

df = pd.DataFrame(pd.read_csv('sentiment_score.csv'))
rob = df['SentimentScore_Roberta']
tb = df['SentimentScore_TextBlob']
vd = df['SentimentScore_Vader']
df['final_score'] = rob

for x in range(len(rob)):
    if rob[x]<0:
        df['final_score'][x]=min(-0.5, rob[x])
    else:
        df['final_score'][x]= (tb[x]+vd[x])/2
df['classification'] = df.final_score.apply(classify)

df.to_csv("final.csv", index=False) 
