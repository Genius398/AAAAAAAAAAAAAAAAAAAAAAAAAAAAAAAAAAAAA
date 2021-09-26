 month = ("January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
 profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000)


 maxProfit = max(profits)
 maxProfitIndex =  profits.index(maxProfit)
 print(maxProfitIndex)

 maxProfitMonth = month[maxProfitIndex]
 print("Max profit was in " + str(maxProfitMonth))


 minProfit = min(profits)
 minProfitIndex = profits.index(minProfit)
 print(minProfitIndex)

 minProfitMonth = month[minProfitIndex]
 print("Min profit was in " + str(minProfitMonth))
 
 yearProfit=20000 + 45000 + 78000 + 97000 + 12000 + 456000 + 65000 + 54000 + 10000 + 30000 + 70000
 avrageProfit=yearProfit/12
 
 print("Year profit was " + str(avrageProfit))