#
from matplotlib import pyplot as plt
import pandas as pd


Data = {
    'Name': ['Amit','Sagar','Pooja'],
    'Math': [85, 90,78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(Data)

print("Shape of Data",df.shape)

print("Column names :", list(df.columns))

print("Data types of each column : ")
print(df.dtypes)    

df.describe()

df['Total'] = df['Math'] + df['Science'] + df['English']

highScore = df[df['Science'] > 85]
print("Students with Science score greater than 85 : ")
print(highScore)

df['Name'] = df['Name'].replace('Pooja','Puja')
print(df['Name'])

sortTotal = df.sort_values(by='Total',ascending=False)
print(sortTotal)


plt.figure(figsize=(7,5))

for sp in df['Name'].unique():
    temp = df[df['Name'] == sp]
    plt.bar(temp['Name'],temp['Total'])
plt.title("Bar Plot")

plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.legend()
plt.grid()
plt.show()


plt.figure(figsize=(7,5))

amit_scores = df[df['Name'] == 'Amit'][['Math','Science','English']].values.flatten()

subjects = ['Math','Science','English']

# Plot line chart
plt.plot(subjects, amit_scores, marker='o', linestyle='-', color='blue', label='Amit')

plt.title("Line Chart - Amit's Subject Scores")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.grid()
plt.show()


df = df.drop('English', axis=1)
print(df.columns)
