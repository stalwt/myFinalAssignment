import pandas as pd
import matplotlib.pyplot as plt
#read the csv file
data_file = pd.read_csv('finance_liquor_sales_2016_2019.csv')
#group the data based on store, bottle retail (percentage) and zip code and get the sum of bottles sold
popural_item = data_file.groupby(["store_name","state_bottle_retail","zip_code"]).bottles_sold.sum()

#create graph
#get the sum of bottles sold based on zip code and show it on plot graph
zip_code_data = data_file.groupby("zip_code").bottles_sold.sum()
plt.plot(zip_code_data.index,zip_code_data,"o")
plt.title('Bottles Sold')
plt.ylabel('Bottles Sold')
plt.xlabel('Zip Code')
plt.show()

#Question: How to get the sum ans then the max value?
