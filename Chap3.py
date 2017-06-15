from matplotlib import pyplot as plt
from collections import Counter

# Plot, line chart:
#     years = [1950,1960,1970, 1980, 1990, 2000, 2010]
#     gdp = [200.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#
#     plt.plot(years,gdp,color='green',marker='o',linestyle='solid')
#
#     plt.title('Nominal GDP')
#
#     plt.ylabel('billions of $')
#
#     plt.show()

# Bar Chart:
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
#



grades= [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade:grade #decile is the individual element in grades

histogram = Counter(decile(grade)for grade in grades)

plt.bar([x-4 for x in histogram.keys()], histogram.values(),8)

plt.axis([-5,105,0,5]) # x-axis from -5 to 105, y-axis from 0 to 5

plt.xticks([10*i for i in range(11)]) # xtricks is the function for x-axis labels
plt.xlabel('Decile')
plt.ylabel('# of students')
plt.title('Distribution of grades')
plt.show()



