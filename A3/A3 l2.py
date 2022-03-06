# ITP 270 Group 3
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl","bob", "mohawk","flattop"]
prices = [30,25,40,20,20,35,50,35]
last_week = [2,3,5,8,4,4,6,2]
total_price = 0
# changes list into int values to go through loop
for price in prices:
    total_price+=price 
# added round to keep decimals short 
average_price= round(total_price/len(prices),2)
print("Average Haircut Price: $" + str(average_price))
new_prices =[price -5 for price in prices]
# Here are the updated prices after decreasing by 5 dollars
print(new_prices)
# revenue 
total_revenue = 0
# range is starting from index value 0 and going up to the length value of this list 
for i in range(len(hairstyles)): 
    total_revenue = prices[i] + last_week[i]
print("Total Revenue: $"+ str(total_revenue))
average_daily_revenue = round((total_revenue/7),2)
print ( "Average Daily Revenue: $" + str(average_daily_revenue))
# we found the haircuts that are under $30
cuts_under_30 = [new_prices[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]
print(cuts_under_30)
print(hairstyles[1]+ " "+ hairstyles[2])