
import matplotlib.pyplot as plt
import pandas as pd

# cities of interest
my_cities = ['Agoura Hills city', 'Yorba Linda city', 'San Jose city', 'San Diego city', "Palm spring city", "Bakersfield city"]


# Load in the data with read_csv()
df = pd.read_csv("Local_Area_Unemployment_Statistics__LAUS___Annual_Average.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique cities
unique_cities = df['Area Name'].unique()

# Plot the data on a line graph
for c in unique_cities:
  if c in my_cities:
    
    # match cities to one of our we want to look at and get a list of years
    years = df[df['Area Name'] == c]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Area Name'] == c]['Unemployment Rate']

    plt.plot(years, sum_elec, label=c)




plt.ylabel('Percentage of City Unemployment Rate')
plt.xlabel('Year')
plt.title('Percent of Population With Umemployment')
plt.legend()
plt.show()
