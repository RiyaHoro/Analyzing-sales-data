import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('sales_data.csv')

# Add a new column 'Total Sales'
df['Total Sales'] = df['Quantity'] * df['Price']

# Total sales over the period
total_sales = df['Total Sales'].sum()
print(f"Total Sales: ${total_sales:.2f}")

# Find the most sold product
product_sales = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print("\nMost Sold Products:")
print(product_sales)

# Generate sales trend over time (line plot)
df['Date'] = pd.to_datetime(df['Date'])
sales_over_time = df.groupby('Date')['Total Sales'].sum()

plt.figure(figsize=(10, 6))
sales_over_time.plot(kind='line', color='blue')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()
plt.savefig('sales_trend.png')

# Sales distribution per product (bar chart)
product_sales.plot(kind='bar', color='green', figsize=(8, 5))
plt.title('Sales Distribution by Product')
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.show()
plt.savefig('sales_Distribution.png')
# Pie chart of sales percentages per product
product_sales_percentage = product_sales / product_sales.sum() * 100
product_sales_percentage.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), startangle=90)
plt.title('Sales Percentage by Product')
plt.ylabel('')
plt.show()
plt.savefig('Sales_percentage.png')
