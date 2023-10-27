"""
: Using the class heights file from last class:
1) Plot the heights in cm as a line plot in matplotlib
2) Plot the average height of males against females in the class using a scatterplot in either seaborn or matplotlib
3) Create a separate column in the data frame to hold the difference from the mean height. 
Plot the difference from the mean against the heights on the same plot.

"""

from scipy.cluster import hierarchy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('class_heights.txt',delimiter='|')
df.columns = df.columns.str.title()
df = df.sort_values(by=['Gender'])
df.index = [i for i in range(0,160)]


# convert feet to cm
def convert_height(height_str):
    # converts height to list of ints [feet, inches]
    feet, inches = map(int, height_str.split("'"))
    total_inches = feet * 12 + inches
    return total_inches * 2.54
df['Height'] = df['Height'].apply(convert_height)
df

female_data_frame = df[df['Gender']=='female']
female_data_frame=female_data_frame.sort_values(by='Height')
male_data_frame = df[df['Gender']=='male']
male_data_frame = male_data_frame.sort_values(by='Height')
x = [i for i in range(0,80)]  # Use the index of the DataFrame as 'x'
female_data_frame.index = x
print(female_data_frame)
male_data_frame.index = x
print(male_data_frame)


# Plot the first line graph from df1
plt.plot(x, male_data_frame['Height'], label='Male', color='red')

# Plot the second line graph from df2
plt.plot(x, female_data_frame['Height'], label='Female', color='blue')
# Add labels and a legend
plt.xlabel('Number of Students')
plt.ylabel('Heights (cm)')
plt.legend()

# Show the plot
plt.title('Class Heights (Gender)')
plt.show()



# Create a line plot
# plt.plot(x, df['Height'])





# # Adding labels and title
# plt.xlabel('Students')
# plt.ylabel('Heights (cm)')
# plt.title('Class Heights')

# # Display the plot
# plt.show()



# # Average Heights
# average_heights = df.groupby('Gender')['Height'].mean()
# gender = ['Female', 'Male']
# heights =  [average_heights['female'], average_heights['male']]
# average_heights = pd.DataFrame({'Gender': gender, 'Height': heights})
# average_heights
# plt.scatter(x = average_heights.index, y = 'Height',  data = average_heights)
# plt.xlabel('Gender')
# plt.ylabel('Heights (cm)')
# plt.title('Average Class Heights (Gender)')
# plt.show()