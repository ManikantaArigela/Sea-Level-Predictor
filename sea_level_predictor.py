import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():

    # Read data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.scatter(
        df['Year'],
        df['CSIRO Adjusted Sea Level']
    )

    # First regression line
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    result = linregress(x, y)

    slope = result.slope
    intercept = result.intercept

    years_extended = np.arange(1880, 2051)

    predicted_y = slope * years_extended + intercept

    ax.plot(
        years_extended,
        predicted_y,
        color='red',
        label='Best Fit Line (1880-2050)'
    )

    # Second regression line
    recent_data = df[df['Year'] >= 2000]

    x_recent = recent_data['Year']
    y_recent = recent_data['CSIRO Adjusted Sea Level']

    result_recent = linregress(x_recent, y_recent)

    slope_recent = result_recent.slope
    intercept_recent = result_recent.intercept

    recent_years_extended = np.arange(2000, 2051)

    predicted_recent_y = (
        slope_recent * recent_years_extended
        + intercept_recent
    )

    ax.plot(
        recent_years_extended,
        predicted_recent_y,
        color='green',
        label='Best Fit Line (2000-2050)'
    )

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Legend
    ax.legend()

    # Save plot
    fig.savefig('sea_level_plot.png')

    return ax