import pandas as pd

# Load dataset
df = pd.read_csv("metadata.csv")

# Look at first 5 rows
print(df.head())

# Shape of data (rows, columns)
print("Shape:", df.shape)

# Data types
print(df.dtypes)

# Missing values
print(df.isnull().sum())

# Statistics for numeric columns
print(df.describe())
# Drop rows with missing publish_time
df = df.dropna(subset=['publish_time'])

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year
df['year'] = df['publish_time'].dt.year

# Create new column: abstract word count
df['abstract_word_count'] = df['abstract'].fillna("").apply(lambda x: len(x.split()))
import matplotlib.pyplot as plt

# Papers by year
year_counts = df['year'].value_counts().sort_index()
plt.bar(year_counts.index, year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

# Top journals
top_journals = df['journal'].value_counts().head(10)
top_journals.plot(kind='bar')
plt.title("Top Journals")
plt.show()
from wordcloud import WordCloud

titles = " ".join(df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)

plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
