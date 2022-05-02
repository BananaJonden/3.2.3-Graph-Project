
import matplotlib.pyplot as plt
import pandas as pd



my_cities = ['Agoura Hills City', 'Yorba Linda City', 'San Jose City', 'San Diego City', "Palm spring City", "Bakersfield City"]


df = pd.read_csv("Local_Area_Unemployment_Statistics__LAUS___Annual_Average.csv", header=0)    # header=0 means there is a header in row 0

unique_cities = df['Area Name'].unique()

for c in unique_cities:
  if c in my_cities:
    
    years = df[df['Area Name'] == c]['Year']

    sum_unemployment = df[df['Area Name'] == c]['Unemployment Rate']

    plt.plot(years, sum_unemployment, label=c)


# TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years

min_anomaly = temp_data['Anomaly'][0]
max_anomaly = temp_data['Anomaly'][0]
min_year = temp_data['Year'][0]
max_year = temp_data['Year'][0]
sum_anomaly = 0
avg_anomaly = 0

# find the min, max and calculate the sum
for i in range(len(temp_data['Anomaly'])):
  if (temp_data['Anomaly'][i] < min_anomaly):
    min_anomaly = temp_data['Anomaly'][i]
    min_year = temp_data['Year'][i]

      # new code inside the same for loop
  if (temp_data['Anomaly'][i] > max_anomaly):
    max_anomaly = temp_data['Anomaly'][i]
    max_year = temp_data['Year'][i]

    sum_anomaly += temp_data['Anomaly'][i]

# calculate average
avg_anomaly = sum_anomaly/len(temp_data['Anomaly'])



plt.ylabel('Percentage of City Unemployment Rate')
plt.xlabel('Year')
plt.title('Percent of Population With Unemployment')
plt.legend()
plt.show()
