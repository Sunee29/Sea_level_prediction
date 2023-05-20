import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def sea_level_analysis():
    # Step 1: Import the data using Pandas
    data = pd.read_csv('epa-sea-level.csv')

    # Step 2: Create a scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Step 3: Get the line of best fit for the entire dataset
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    line = slope * data['Year'] + intercept
    plt.plot(data['Year'], line, color='r', label='Line of Best Fit')

    # Step 4: Get the line of best fit for the data from year 2000 onwards
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    line_recent = slope_recent * data['Year'] + intercept_recent
    plt.plot(data['Year'], line_recent, color='g', label='Line of Best Fit (Since 2000)')

    # Step 5: Predict sea level rise in 2050
    future_year = 2050
    predicted_sea_level = slope * future_year + intercept
    predicted_sea_level_recent = slope_recent * future_year + intercept_recent

    plt.plot(future_year, predicted_sea_level, 'bo', label=f'Predicted Sea Level in {future_year} (All Data)')
    plt.plot(future_year, predicted_sea_level_recent, 'go', label=f'Predicted Sea Level in {future_year} (Since 2000)')

    plt.legend()
    plt.savefig('sea_level_plot.png')
    plt.show()

if __name__ == "__main__":
    sea_level_analysis()
