#secondo caso di studio, rendiconto di un investimento

startBalance = float(input('Insert the investment amount: '))
years = int(input('Insert the number of years: '))
rate = int(input('insert the rate as a %: '))

rate = rate / 100
totalInterest = 0.0

print('%4s%18s%10s%16s ' %  \
    ("years", "Starting Balance", "Interest", "Ending Balance"))

for years in range(1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print('%4d%18.2f%10.2f%16.2f ' % \
        (years,startBalance,interest,endBalance))
    startBalance = endBalance
    totalInterest += interest
    
print('Ending balance is $%0.2f' % endBalance)
print('Total interest are $%0.2f' % totalInterest)
