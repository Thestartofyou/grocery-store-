import matplotlib.pyplot as plt

# Sample grocery store receipt data
receipts = [
    {'date': '2023-05-01', 'item': 'Apple', 'price': 0.99},
    {'date': '2023-05-02', 'item': 'Banana', 'price': 0.89},
    {'date': '2023-05-03', 'item': 'Orange', 'price': 1.19},
    {'date': '2023-05-04', 'item': 'Apple', 'price': 0.99},
    {'date': '2023-05-05', 'item': 'Banana', 'price': 0.79},
    {'date': '2023-05-06', 'item': 'Orange', 'price': 1.29},
    # Add more receipt entries...
]

# Track price changes over time
prices = []
dates = []

for receipt in receipts:
    prices.append(receipt['price'])
    dates.append(receipt['date'])

# Create line plot using Matplotlib
plt.plot(dates, prices, marker='o')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Price Trend of Grocery Store Receipts')
plt.xticks(rotation=45)
plt.show()
