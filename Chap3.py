from matplotlib import pyplot as plt
from collections import Counter

# Plot, line chart:
'''
     years = [1950,1960,1970, 1980, 1990, 2000, 2010]
#     gdp = [200.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#
#     plt.plot(years,gdp,color='green',marker='o',linestyle='solid')
#
#     plt.title('Nominal GDP')
#
#     plt.ylabel('billions of $')
#
     plt.show()
'''


# Bar Chart:
'''
# movies = ['Annie Hall', 'Ben-Hur','Casablanca', 'Gandhi', 'West Side Story']
# num_oscars = [5,11,3,8,10]
#
# xs = [i+0.1 for i,_ in enumerate(movies)] #the x coordinate
#
# plt.bar(xs,num_oscars)
#
# plt.ylabel('# of Academy Awards')
# plt.title('Movies')
#
# plt.xticks([i+0.1 for i,_ in enumerate(movies)],movies) # first argument is the coordinate, second is the text
#
# plt.show()
'''


'''
grades= [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade:grade//10 *10  #decile is the individual element in grades

histogram = Counter(decile(grade)for grade in grades)

plt.bar([x-4 for x in histogram.keys()], histogram.values(),8)

plt.axis([-5,105,0,5]) # x-axis from -5 to 105, y-axis from 0 to 5

plt.xticks([10*i for i in range(11)]) # xtricks is the function for x-axis labels
plt.xlabel('Decile')
plt.ylabel('# of students')
plt.title('Distribution of grades')
plt.show()
'''

#Line Chart:
'''
variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256,128,64,32,16,8,4,2,1]
total_error = [x+y for x,y in zip(variance,bias_squared)]
xs = [i for i,_ in enumerate(variance)]
    
# plot multiple lines on one chart:
plt.plot(xs,variance,'g-', label='variance') # g- means green solid line
plt.plot(xs,bias_squared,'r-.',label = 'bias^2') # r-. means red dot-dashed line
plt.plot(xs,total_error, 'b:', label = 'total error') # b: means blue dotted line

plt.legend(loc=9) # loc=9 means 'top center' - put the line explanation on top center (like variance is green solid line) 
plt.xlabel('mmodel complexity')
plt.title('The Bias-Variance Tradeoff')
plt.show()
'''

# Scatter Plots:
'''
friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends,minutes)

plt.axis([58,74,80,240])


    #label each point:
for label, friend_count, minute_count in zip(labels,friends,minutes):
    plt.annotate(label, xy=(friend_count,minute_count), # put the label on point xy, which is friend_count,minute_count
                 xytext=(5,-5), # but the text(label) is slightly off the point (not exactly on the point)
                 textcoords = 'offset points')

plt.title('Daily Minutes vs. Number of Friends')
plt.xlabel('# of friends')
plt.ylabel('daily minutes spent on the site')
plt.show()
'''

