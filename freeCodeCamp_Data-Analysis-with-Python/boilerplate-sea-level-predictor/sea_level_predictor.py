import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
  
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
  
    # Create first line of best fit
    first_line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    first_x = np.arange(df['Year'].min(),2051,1)
    first_y = first_x*first_line.slope + first_line.intercept
  
    plt.plot(first_x,first_y)
  
    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
  
    second_line = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    second_x = np.arange(2000,2051,1)
    second_y = second_x*second_line.slope + second_line.intercept
  
    plt.plot(second_x,second_y)
  
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()