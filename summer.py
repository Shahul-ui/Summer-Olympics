import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('summer.csv')

# Q1 - In how many cities Summer Olympics is held so far?
print('Q1 -', len(df['City'].unique()))

# Q2 - Which sport is having most number of Gold Medals so far? (Top 5)
data = []
for p in df.loc[df['Medal'] == 'Gold', 'Sport'].value_counts().items():
	data.append(p)
pd.DataFrame(data, columns = ['Sport', 'freq']).sort_values(by = 'freq', ascending = False).head().plot(x = 'Sport', y = 'freq', kind = 'bar', figsize = (5, 5))

# Q3 - Which sport is having most number of medals so far? (Top 5)
data = []
for p in df['Sport'].value_counts().items():
	data.append(p)
pd.DataFrame(data, columns = ['Sport', 'freq']).sort_values(by = 'freq', ascending = False).head().plot(x = 'Sport', y = 'freq', kind = 'bar', figsize = (5, 5))

# Q4 - Which player has won most number of medals? (Top 5)
data = []
for p in df['Athlete'].value_counts().items():
	data.append(p)
pd.DataFrame(data, columns = ['Athlete', 'freq']).sort_values(by = 'freq', ascending = False).head().plot(x = 'Athlete', y = 'freq', kind = 'bar', figsize = (5, 5))

# Q5 - Which player has won most number Gold Medals of medals? (Top 5)
data = []
for p in df.loc[df['Medal'] == 'Gold', 'Athlete'].value_counts().items():
	data.append(p)
pd.DataFrame(data, columns = ['Athlete', 'freq']).sort_values(by = 'freq', ascending = False).head().plot(x = 'Athlete', y = 'freq', kind = 'bar', figsize = (5, 5))

# Q6 - In which year India won first Gold Medal in Summer Olympics?
print('Q6 -', df.loc[(df['Country'] == 'IND')&(df['Medal']=='Gold'),'Year'].values[0])

# Q7 - Which event is most popular in terms on number of players? (Top 5)
data = []
for p in df['Event'].value_counts().items():
	data.append(p)
pd.DataFrame(data, columns = ['Event', 'freq']).sort_values(by = 'freq', ascending = False).head().plot(x = 'Event', y = 'freq', kind = 'bar', figsize = (5, 5))

# Q8 - Which sport is having most female Gold Medalists? (Top 5)
data = []
for p in df.loc[df['Gender'] == 'Women', 'Sport'].value_counts().items():
	data.append(p)
pd.DataFrame(data, columns = ['Sport', 'freq']).sort_values(by = 'freq', ascending = False).head().plot(x = 'Sport', y = 'freq', kind = 'bar', figsize = (5, 5))

plt.show()
