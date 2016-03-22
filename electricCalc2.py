print('Electricity bill estimator 2.0')
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff=int(input('Which tariff?? 11 or 31:'))
use=float(input('Enter daily use in kWh:'))
billDay=int(input('Enter number of billing days:'))

if tariff == 11:
    total=TARIFF_11*use*billDay
elif tariff == 31:
    total=TARIFF_31*use*billDay
else:
    print('Error')

print('Estimated bill: $',round(total,2))