import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# getting csv file
data = pd.read_csv("https://raw.githubusercontent.com/raunak101172/projects/master/billionares.csv")
print(data.head())
# checking if any table has empty values
print(data.isnull().sum())
# dropping the null values
data = data.dropna()
# removing $,B and making all networths as floats
data["NetWorth"] = data["NetWorth"].str.strip("$")
data["NetWorth"] = data["NetWorth"].str.strip("B")
data["NetWorth"] = data["NetWorth"].astype(float)
# top 10 billionares net worth
df = data.sort_values(by = ["NetWorth"], ascending=False).head(10)
plt.figure(figsize=(20, 10))
sns.histplot(x="Name", hue="NetWorth", data=df)
plt.show()
# top 5 domains with most number of billionares
a = data["Source"].value_counts().head()
index = a.index
sources = a.values
custom_colors = ["blue", "purple", 'yellow', "green", "red"]
plt.figure(figsize=(5, 5))
plt.pie(sources, labels=index, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Domains to Become a Billionaire", fontsize=20)
plt.show()
# top 5 industries with most number of billionares
a = data["Industry"].value_counts().head()
index = a.index
industries = a.values
custom_colors = ["blue", "purple", 'yellow', "green", "red"]
plt.figure(figsize=(5, 5))
plt.pie(industries, labels=index, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Industries with Most Number of Billionaires", fontsize=20)
plt.show()
# top 5 countries with most billionares
a = data["Country"].value_counts().head()
index = a.index
Countries = a.values
custom_colors = ["blue", "purple", 'yellow', "green", "red"]
plt.figure(figsize=(5, 5))
plt.pie(Countries, labels=index, colors=custom_colors)
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size=12)
plt.title("Top 5 Countries with Most Number of Billionaires", fontsize=20)
plt.show()
