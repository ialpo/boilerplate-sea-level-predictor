import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv ( 'epa-sea-level.csv' )

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter( x, y )

    m, y0, r, p, std_err = linregress ( x, y )

    minYear = df['Year'].min()

    def linear ( x ):
        return m * x + y0

    xSlope1 = list(range(minYear, 2050))
    ySlope1 = list(map ( linear, xSlope1 ))

    plt.plot ( xSlope1, ySlope1 )

    index2000 = x.index[ x == 2000 ][0]

    x2000 = x[index2000:]
    y2000 = y[index2000:]
    
    m, y0, r, p, std_err = linregress ( x2000, y2000 )

    xSlope2 = list ( range(2000, 2050) )
    ySlope2 = list ( map ( linear, xSlope2 ) )

    plt.plot ( xSlope2, ySlope2 )

    plt.title ( 'Rise in Sea Level' )
    plt.xlabel ( 'Year' )
    plt.ylabel ( 'Sea Level (inches)' )
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()