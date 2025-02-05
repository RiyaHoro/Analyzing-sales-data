import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('sales_data.csv')

# Plotting the bar chart
plt.bar(data['Product'], data['Price'])
plt.xlabel('Product')
plt.ylabel('Price')
plt.title('Price by Product')
plt.show()
plt.savefig('Product_prices.png')