def revenue(prevrev,growthrate):
 return prevrev*(1+growthrate/100) # Major driver is store count,LFL growth, Promtion intensity and Seasonality (holidays and stuff)

x = float(input("Enter the revenue for the previous month:"))
y = float(input("Enter the growth rate(%) for the current month:"))
 
print(f"The current month's revenue is: {revenue(x, y):,.2f}")
