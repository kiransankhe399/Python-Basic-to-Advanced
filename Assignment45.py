from matplotlib import pyplot as plt
import pandas as pd


Data = {
    'Name': ['Amit','Sagar','Pooja'],
    'Math': [85, 90,78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}


df = pd.DataFrame(Data)

df['Math_Normalized'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())


df['Gender'] = ['Male', 'Male', 'Female']
encodedGender = pd.get_dummies(df, columns=['Gender'],dtype=int)
print(encodedGender)

avg = df.groupby('Gender').mean(numeric_only=True)
print(avg)

sagar = df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].iloc[0]
plt.pie(sagar, labels=sagar.index, autopct='%1.1f%%', startangle=90)
plt.title("Subject Marks for Sagar")
plt.show()


df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)
df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')

passed_count = df[df['Status'] == 'Pass'].shape[0]
print("Students Passed:", passed_count)


df.to_csv('Final_Student_Data.csv', index=False)


plt.hist(df['Math'], bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram of Math Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()


df.rename(columns={'Math': 'Mathematics'}, inplace=True)


plt.boxplot(df['English'])
plt.title("Boxplot of English Marks")
plt.ylabel("Marks")
plt.show()

