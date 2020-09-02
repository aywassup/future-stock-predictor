import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import datetime as DT
import statistics
#this section gives historical data of a company and visualizes the data into a scatterplot
msft = yf.Ticker("GILD")

days = input("how many days?: ")
hist = msft.history(period=days + "d")
print(hist)
dates = []
today = DT.date.today()
n = days
end = 0

for i in range(int(days)):
	dates.append(i)
prices = hist['Open'].to_list()

#calculating for the multiplier to predit future data
p = 0
for i in range(len(prices)-1):
	p += prices[i-1] / prices[i]
p = p/(len(prices)-1)

#multiplies past data to a multiplier to predit future data
future_data = []
for i in range(len(prices)):
	future_data.append(prices[-1] * (p**i))

#saves future scatter plot
scatter = sns.regplot(dates,future_data)
plt.savefig('future_stock.png')
plt.clf()

#saves past scatter plot
scatter = sns.regplot(dates,prices)
plt.savefig('stock.png')
plt.clf()

#this section predits future data
#find the slope from the start date and the end date, and then just draw a straight line in another graph

#compare different categories average employees, how fast companies are growing
companies_tech = ["GILD", "MSFT", "GOOGL"]
companies_stores = ["WMT", "TGT", "BBY"]
companies_supermarket = ["KR", "ACI", "COST"]

a = []
for company in companies_tech:
	msft = yf.Ticker(company)
	hist = msft.history(period="1d")
	a.append(hist['Open'].to_list()[0])

b = []
for company in companies_stores:
	msft = yf.Ticker(company)
	hist = msft.history(period="1d")
	b.append(hist['Open'].to_list()[0])

c = []
for company in companies_supermarket:
	msft = yf.Ticker(company)
	hist = msft.history(period="1d")
	c.append(hist['Open'].to_list()[0])

d = {'Tech Companies':a,'Retail':b, 'Supermarket': c}
df = pd.DataFrame(data=d)
barplot = sns.barplot(data=df,ci=None)
barplot.set(title="Companies",xlabel="Type",ylabel="Stock Price")
plt.savefig('companies.png')



"""
add documentation to the code
add a third category
make it neater
"""
