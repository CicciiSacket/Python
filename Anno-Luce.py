#calcolare e visualizzare il valore di un anno luce

Minute_day = 24 * 60
Second_day =  Minute_day * 60
Second_year = Second_day * 365

Value = ((3 * pow(10,8) * Second_year))

print("Il valore di un anno luce è: " + str(Value) + " metri al secondo" )