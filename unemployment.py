import matplotlib.pyplot as plt
import pandas as pd



my_cities = ['Agoura Hills City', 'Yorba Linda City', 'San Jose City', 'San Diego City', "Palm spring City", "Bakersfield City"]


unemployment = pd.read_csv("Local_Area_Unemployment_Statistics__LAUS___Annual_Average.csv", header=0)    # header=0 means there is a header in row 0

unique_cities = unemployment['Area Name'].unique()

for c in unique_cities:
  if c in my_cities:
    
    years = unemployment[unemployment['Area Name'] == c]['Year']

    sum_unemployment = unemployment[unemployment['Area Name'] == c]['Unemployment Rate']

    plt.plot(years, sum_unemployment, label=c)


'''
min_unemployment = unemployment['Unemployment Rate'][0]
max_unemployment = unemployment['Unemployment Rate'][0]
min_year = unemployment['Year'][0]
max_year = unemployment['Year'][0]
sum_unemployment = 0
avg_unemployment = 0

# find the min, max and calculate the sum
for i in range(len(unemployment['Unemployment Rate'])):
  if (unemployment['Unemployment Rate'][i] < min_unemployment):
    min_unemployment = unemployment['Unemployment Rate'][i]
    min_year = unemployment['Year'][i]

      # new code inside the same for loop
  if (unemployment['Unemployment Rate'][i] > max_unemployment):
    max_unemployment = unemployment['Unemployment Rate'][i]
    max_year = unemployment['Year'][i]

    sum_unemployment += unemployment['Unemployment Rate'][i]

# calculate average
avg_unemployment = sum_unemployment/len(unemployment['Unemployment Rate'])

'''

palm_spring_average = (11.8+11.1+9.8+8.3+6.8+5.5+5.6+4.7+4.1+3.8+10.7)
agoura_hills_average = (10.5+10.2+9.2+8.1+6.8+5.5+4.8+4.1+4.3+4+10.3)
yorba_linda_average = (8.8+8.2+7.1+5.9+4.9+3.9+3.7+3.3+2.8+2.6+7.2)
san_jose_average = (11.8+10.5+8.9+7.3+5.8+4.7+3.9+3.4+2.8+2.7+8.1)
san_diego_average = (10.5+10+8.8+7.6+6.2+5+4.6+3.9+3.+ 3.1+9)
bakersfield_average = (14.4+13.5+12+10.6+9.4+9.2+7.8+6.5+5.6+5.4+11.2)

minimum = 2.6
maximum = 14.4
total_average = palm_spring_average + agoura_hills_average + yorba_linda_average + san_jose_average + san_diego_average + bakersfield_average
total_average = total_average/55
print("the total average of unemployment:",total_average)
print("the minimum:", minimum)
print("the maximum:", maximum)

plt.ylabel('Percentage of City Unemployment Rate')
plt.xlabel('Year')
plt.title('Percent of Population With Unemployment')
plt.legend()
plt.show()
'''
print("The maximum Unemployment:", max_unemployment, "which occured in", max_year)
print("The minimum Unemployment:", min_unemployment, "which occured in", min_year)
print("The average Unemployment:", avg_unemployment)
'''
