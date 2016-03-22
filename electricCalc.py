print('Electricity bill estimator')

cents=float(input('Enter cents per kWh:'))
use=float(input('Enter daily use in kWh:'))
billDay=int(input('Enter number of billing days:'))


total=cents/100*use*billDay


print('Estimated bill: $',total)
