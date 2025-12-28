import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Roll_No': [1, 2, 3, 4, 5],
    'Name': ['Aman', 'Riya', 'Piyush', 'Neha', 'Rahul'],
    'Total_Classes': [50, 50, 50, 50, 50],
    'Classes_Attended': [45, 40, 48, 35, 42]
}

df = pd.DataFrame(data)
print(df)

df['Attendance_Percentage'] = np.round(
    (df['Classes_Attended'] / df['Total_Classes']) * 100, 2
)

print(df)

df['Status'] = np.where(df['Attendance_Percentage'] >= 75, 'Present', 'Shortage')

print(df)

df.to_csv('attendance_report.csv', index=False)
print("Attendance report saved successfully")

plt.figure()
plt.bar(df['Name'], df['Attendance_Percentage'])
plt.xlabel('Student Name')
plt.ylabel('Attendance Percentage')
plt.title('Student Attendance Report')
plt.show()
