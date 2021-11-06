# Exercises from Chapter 2
#
# Handy Dandy Links I found:
# PyPlot Main Documentation: https://matplotlib.org/stable/api/pyplot_summary.html
# Plot (I call chart): https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
# LineChart: https://matplotlib.org/stable/api/_as_gen/matplotlib.lines.Line2D.html
# Markers: https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
# LineStyles: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
#

from matplotlib import pyplot as chart
years = [1950, 1960, 1970, 1980 , 1990 , 2000, 2010]
gdp = [ 300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Create a line chart years on x-axis, gdp on y axis
chart.plot(years, gdp, color='green', marker='o', linestyle='solid') # x, y, color, marker, linestyle (can also be dashed)
chart.title("nomial GDP") # Add a title
chart.ylabel("Billion of $") #Add a label to the y-axis
chart.show()

# Creates Bar chart
movies = ["Annie Hall", "Ben-Hur", "Casablance", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]
xs = [i + 0.1 for i, _ in enumerate(movies)] # Bars are .8 in width so a 0.1 is for spacing.
chart.bar(xs, num_oscars) # This makes it a bar chart
chart.ylabel("# of Academy Awards")
chart.title("My Favorite Movies")
chart.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
chart.show()

# The structure for ticks is value first, followed by label: matplotlib.pyplot.xticks(ticks=None, labels=None, **kwargs). No label, number is default
# Try to keep the starting point of Y zero as other values may cause distortion. (i.e. playing with appearances by axis)
from collections import Counter
grades = [83,95,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)
chart.bar([ x - 4 for x in histogram.keys()], histogram.values(), 8) # Shift bars by 4, give correct height, give each bar the width of 8
chart.axis([-5, 105, 0, 5]) # x axis is from -5 to 105 and y axis is 0 to 5 (x-start, x-end, y-start, y-end)
chart.xticks([10 * i for i in range(11)]) # x axis grows by segment of 10
chart.xlabel("Decile")
chart.ylabel("# of Students")
chart.title("Distrobution of Exam 1 Grades")
chart.show()

# Shows multiple overlapping line charts
variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x + y for x, y in zip(variance,bias_squared)]
xs = [i for i, _ in enumerate(variance)] # xs is the x scale

# ?????????????????????????????????????????????????????????????????????????
# What are variances and Bias? What are they used for and how to find them?
# ?????????????????????????????????????????????????????????????????????????
chart.plot(xs, variance, 'g-', label='variance') # green solid line
chart.plot(xs, bias_squared, 'r-.', label='bias^2') # red dot-dashed line
chart.plot(xs, total_error, 'b:', label='total error') # blue dotted line

# chart.legend(loc=4) # Location of Legend value are here : https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
chart.xlabel("model complexity")
chart.title("The Bias-Variance Tradeoff")
chart.show()

# Scatter Plot Example
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67] 
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a','b','c','d','e','f','g','h','i']

chart.scatter(friends, minutes)
# ?????????????????????????????????????????????????????????????????????????
# Chart meta destroy the data from the chart annotations, but why?
# ?????????????????????????????????????????????????????????????????????????
for label, friend_count, minute_count in zip(labels,friends, minutes):
    chart.annotate(label, xy = (friend_count, minute_count), xytext = (5,-5), textcoords='offset points')
#Create Metadata
chart.title("Daily Minutes vs Number of Friends")
chart.xlabel("# of friends")
chart.ylabel("daily minutes spent on site")
chart.show()
