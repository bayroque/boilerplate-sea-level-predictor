import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x,y=df['Year'],df['CSIRO Adjusted Sea Level']
    plt.scatter(x,y)

    # Create first line of best fit
    slope = linregress(df['Year'],df['CSIRO Adjusted Sea Level']).slope
    intercept = linregress(df['Year'],df['CSIRO Adjusted Sea Level']).intercept
    predict_years = pd.Series(range(1880,2051))
    plt.plot(predict_years, intercept + slope*predict_years, 'r', label='first line of best fit')

    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    years2000 = pd.Series(range(2000,2051))
    slope2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level']).slope
    intercept2 = linregress(df2['Year'],df2['CSIRO Adjusted Sea Level']).intercept
    plt.plot(years2000, intercept2 + slope2*years2000, 'y', label='second line of best fit')

    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()