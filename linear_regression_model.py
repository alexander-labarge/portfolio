#!/usr/bin/env python3
""" This is a module I wrote to achieve modeling for U.S. Energy Production
utilizing the least squares linear regression modeling equation. It uses pandas
to read an excel file, extract the data for plotting. Then the linear regression
equation is deducted from the values. The user is then able to input either a year
to determine U.S. Energy Production, or a production amount to determine by 
what year the U.S. will achieve the enery production amount.
"""

__author__ = "Alexander La Barge"
__copyright__ = "Copyright 2022"
__date__ = "2022/08/30"
__deprecated__ = False
__email__ =  "labargeam@gmail.com"
__license__ = "GPLv3"
__maintainer__ = "Alexander La barge"
__status__ = "Production"
__version__ = "0.0.1"

# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
  
# x axis values
x = [1950, 1960, 1970, 1980, 1990, 2000]
# corresponding y axis values
y = [35.6, 42.8, 63.5, 67.2, 70.7, 71.2]
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('Year')
# naming the y axis
plt.ylabel('Production (In Quads)')
  
# giving a title to my graph
plt.title('Energy Production Data Graph')

# function to show the plot
# plt.show()

print('\n')

print('''
Alexander La Barge, 30 Aug 2022, MATH 115 6380 Pre-Calculus
Section 2.5: Regression, Problem # 3
\n
I did not have a graphing calculator handy, so I have utilized the python
programming language to assist me.

Answers:

Answer A) Plot the graph: \n ''')
plt.show()

print('''
Answer B) From the historical perspective, we can ignore the first two datapoints
relative to the 1950s and 1960s becuase during that time period, nearly a third
of all US power was hydroelectric. This coupled with the secondary effects of
the great depression gave cause for decreased energy demand/ hence decreased
energy production requirements.
''')
# Time to pull the data from our Excel File
data = pd.read_csv('/usr/local/energy_data.csv')
# - used this command to understasnd the shape, then commented it out
# print(data.shape)
print("Before we move on, let's see our data to see if python parsed it correctly. \n")
print(data.head(), "\n")

# Time to assign our X and Ys again.

# Assigning X and Y
X = data['Year'].values
Y = data['Production'].values
print('X values stored as: ', X)
print('Y values stored as: ', Y, "\n")

print('Now we must calculate slope and y-intercept. First we need the means of X and Y.')
# Mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)
print()
print('Mean of X = ', mean_x)
print('Mean of Y =', mean_y)
 
# Total number of values
n = len(X)

# Using the formula to calculate 'm' and 'c'
numer = 0
denom = 0
for i in range(n):
  numer += (X[i] - mean_x) * (Y[i] - mean_y)
  denom += (X[i] - mean_x) ** 2
  m = numer / denom
  c = mean_y - (m * mean_x)
 
# Printing coefficient
print()
print("Coefficients")
print()
print('Our slope is: ', m)
print('Our intercept value is: ', c, '\n')

# Regression Line Calculation

print('Answer C: ')
print('''Least Squares Regression Line for US Energy Production is:
y= 0.266x???459.86, where:
output = .266(year)-459.86
y = energy production output
x = year input
Note: in my program, y=m(x)+c 
''')
print()

# Calculating R2 Score
ss_tot = 0
ss_res = 0
for i in range(n):
    y_pred = c + m * X[i]
    ss_tot += (Y[i] - mean_y) ** 2
    ss_res += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_res/ss_tot)
if r2 >= .7:
  print('R2 score is:', r2, '\n' "R2 Score is a good fit, with score about 0.7 and we can assume data is showing a high level of correlation")
else: 
  print('R2 score is:', r2, '\n', 'R2 Score is a bad fit, with score below 0.7 and we can assume data is showing a low level of correlation')
print()

print("Let us now plot our regression line: ", '\n')
# Plotting our regression line:

max_x = np.max(X) + 100
min_x = np.min(X) - 100
 
# Calculating line values x and y
x = np.linspace(min_x, max_x, 1000)
y = c + m * x
 
# Ploting Line
plt.plot(x, y, color='#58b970', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')
 
plt.xlabel('Year')
plt.ylabel('Production')
plt.legend()
plt.show()

print('\n')

def prediction_byyear():
  new_x = int(input('Enter a year to preduct the annual U.S. Energy Production: '))
  new_y = ((new_x * m) +c)
  print(' Answer D: ','For the year entered: ', new_x) 
  print('The predicted U.S. Energy Output will be: ', round(new_y, 3),'Quads')
print()

def prediction_byquads():
  output = int(input('Enter the number of Quads to see what year will yield such results: '))
  year = ((output-c)/m)
  print('Answer E: ','For the output entered: ', output)
  print('The predicted year such output will occur is: ', round(year))
print() 



prediction_byyear()
prediction_byquads()
