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



# ///////////////////////////////////////////////////////////////
# Lineplot
# ///////////////////////////////////////////////////////////////
# Female / Male Line Plots 
plt.plot(x, female_data_frame['Height'], label='Female', color='red')
plt.plot(x, male_data_frame['Height'], label='Male', color='blue')

# Add labels and a legend
plt.xlabel('Number of Students')
plt.ylabel('Heights (cm)')
plt.legend()

# Show the plot
plt.title('Class Heights (Gender)')
plt.show()




# ///////////////////////////////////////////////////////////////
# Scatterplot
# ///////////////////////////////////////////////////////////////
# Create a single plot
plt.figure(figsize=(6, 6))
# Female / Male Scatter Points
plt.scatter(female_data_frame['Gender'],female_data_frame['Height'], label='Individual', color='grey', marker='o', alpha=0.5)
plt.scatter(male_data_frame['Gender'],male_data_frame['Height'], color='grey', marker='o', alpha=0.5)

# Average Scatter Points
plt.scatter('Female',female_data_frame['Height'].mean(), label='Average', color='red', marker='o', alpha=0.5,  s=100)
plt.scatter('Male',male_data_frame['Height'].mean(), color='red', marker='o', alpha=0.5,  s=100)

# Add labels and a legend
plt.xlabel('Genders')
plt.ylabel('Height (cm)')
plt.legend()

# Show the plot
plt.title('Class Heights (Gender)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
