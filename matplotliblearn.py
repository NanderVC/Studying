import matplotlib.pyplot as plt
%matplotlib inline
from matplotlib.ticker import MaxNLocator

apl_price = [93.95, 112.15, 104.05, 144.85, 169.49]
ms_price = [39.01, 50.29, 57.05, 69.98, 94.39]
year = [2014, 2015, 2016, 2017, 2018]

#linestyles intuitive :, --, o give lines in those shapes
plt.plot(year, apl_price, ':k'
        year, ms_price, 'g')
plt.xlabel('Year')
plt.ylabel('Stock price')

#plotting min and max for then min and max for y set after each other, so four arguments
plt.axis([2013, 2019, 20, 180)

plt.show()

#new hardcoded figure
#figsize = width, height (inches)
fig_1 = plt.figure(1, figsize = 6.4, 4.8)

#makes two empty charts within the figure
#121 & 122 defines the layout of the cahrts within the figure. 1 row with 2 columns with chart_1 on
#position 1 (121) and chart_2 on position 2 (122). Indezing adds left to right going down columns, so f.e.
# 5 is position 3,1 in the matrix
chart_1 = fig_1.add_subplot(121)
chart_2 = fig_1.add_subplot(122)

#Now we add data
chart_1.plot(year, apl_price)

#To set ticks use MaxNLocator function
chart_1.xaxis.set_major_locator(MaxNLocator(integer=True))
chart_2.scatter(year, ms_price)

#easier way of setting grid with new subplots, again first number is row second column in the arguments
fig_2, axes = plt.subplots(3,2,figsize=(20,5)
#here row and column index neccesary
axes[0, 1].scatter(year, ms_price)
axes[1, 0].plot(year, apl_price)
plt.show