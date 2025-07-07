#calcolare e visualizzare il valore di un anno luce

velocityOfLight = 3 * pow(10,8)

Minute_day = 24 * 60
Second_day =  Minute_day * 60
Second_year = Second_day * 365

Value = ( velocityOfLight * Second_year)

print("Value of one year light is: " + str(Value) + " meters per second" )